"""Minimal reproducible training utilities for EndSurvGAN.

This file mirrors the documented experimental defaults where possible:
Adam optimization, latent dimension 128, WGAN-GP coefficient 10, and
200 training epochs. Dataset-specific preprocessing and the full conditional
survival-consistency regularizer remain experiment-layer responsibilities.
"""

from __future__ import annotations

from dataclasses import dataclass

import torch

from src.losses.survival_losses import (
    bernoulli_kl_from_rates,
    gradient_penalty,
    wasserstein_critic_loss,
    wasserstein_generator_loss,
)


@dataclass
class TrainingConfig:
    latent_dim: int = 128
    lr: float = 2e-4
    epochs: int = 200
    lambda_gp: float = 10.0
    lambda_cens: float = 1.0
    critic_steps: int = 5
    device: str = "cuda" if torch.cuda.is_available() else "cpu"


def pack_survival_sample(x: torch.Tensor, t: torch.Tensor, delta: torch.Tensor) -> torch.Tensor:
    return torch.cat([x, t, delta], dim=1)


def train_one_batch(model, real_x, real_t, real_delta, g_optimizer, d_optimizer, config: TrainingConfig):
    """Perform one WGAN-GP update on a batch.

    Returns a dictionary of scalar losses suitable for experiment logging.
    """
    device = config.device
    real_x = real_x.to(device)
    real_t = real_t.to(device)
    real_delta = real_delta.to(device).float()
    batch_size = real_x.size(0)

    d_loss_value = None
    gp_value = None

    for _ in range(config.critic_steps):
        z = torch.randn(batch_size, config.latent_dim, device=device)
        fake_x, fake_t, fake_delta = model.generator(z)

        real_scores = model.discriminator(real_x, real_t, real_delta)
        fake_scores = model.discriminator(fake_x.detach(), fake_t.detach(), fake_delta.detach())

        real_joint = pack_survival_sample(real_x, real_t, real_delta)
        fake_joint = pack_survival_sample(fake_x.detach(), fake_t.detach(), fake_delta.detach())
        gp = gradient_penalty(model.discriminator, real_joint, fake_joint)
        d_loss = wasserstein_critic_loss(real_scores, fake_scores) + config.lambda_gp * gp

        d_optimizer.zero_grad(set_to_none=True)
        d_loss.backward()
        d_optimizer.step()

        d_loss_value = d_loss.detach()
        gp_value = gp.detach()

    z = torch.randn(batch_size, config.latent_dim, device=device)
    fake_x, fake_t, fake_delta = model.generator(z)
    fake_scores = model.discriminator(fake_x, fake_t, fake_delta)

    adv_loss = wasserstein_generator_loss(fake_scores)
    censoring_loss = bernoulli_kl_from_rates(real_delta.mean(), fake_delta.mean())
    g_loss = adv_loss + config.lambda_cens * censoring_loss

    g_optimizer.zero_grad(set_to_none=True)
    g_loss.backward()
    g_optimizer.step()

    return {
        "generator_loss": float(g_loss.detach().cpu()),
        "adversarial_loss": float(adv_loss.detach().cpu()),
        "censoring_loss": float(censoring_loss.detach().cpu()),
        "critic_loss": float(d_loss_value.cpu()),
        "gradient_penalty": float(gp_value.cpu()),
    }
