"""Loss utilities for EndSurvGAN.

The research summary defines the total objective as:

    L_total = L_adv + lambda_surv L_surv + lambda_cens L_cens

with WGAN-GP adversarial optimization and survival/censoring-aware
regularization. This module provides the adversarial and gradient-penalty
components plus interfaces for experiment-specific survival regularizers.
"""

from __future__ import annotations

import torch


def wasserstein_critic_loss(real_scores: torch.Tensor, fake_scores: torch.Tensor) -> torch.Tensor:
    """Critic loss: E[D(fake)] - E[D(real)]."""
    return fake_scores.mean() - real_scores.mean()


def wasserstein_generator_loss(fake_scores: torch.Tensor) -> torch.Tensor:
    """Generator adversarial loss for WGAN training."""
    return -fake_scores.mean()


def gradient_penalty(discriminator, real_sample: torch.Tensor, fake_sample: torch.Tensor) -> torch.Tensor:
    """Compute the WGAN-GP penalty on interpolated joint survival samples."""
    batch_size = real_sample.size(0)
    alpha = torch.rand(batch_size, 1, device=real_sample.device)
    alpha = alpha.expand_as(real_sample)
    interpolated = alpha * real_sample + (1.0 - alpha) * fake_sample
    interpolated.requires_grad_(True)

    # The critic consumes X, T, delta separately; split by convention.
    x = interpolated[:, :-2]
    t = interpolated[:, -2:-1]
    delta = interpolated[:, -1:]
    scores = discriminator(x, t, delta)

    gradients = torch.autograd.grad(
        outputs=scores,
        inputs=interpolated,
        grad_outputs=torch.ones_like(scores),
        create_graph=True,
        retain_graph=True,
        only_inputs=True,
    )[0]
    gradients = gradients.reshape(batch_size, -1)
    return ((gradients.norm(2, dim=1) - 1.0) ** 2).mean()


def bernoulli_kl_from_rates(real_event_rate: torch.Tensor, fake_event_rate: torch.Tensor, eps: float = 1e-7) -> torch.Tensor:
    """A stable Bernoulli KL utility for censoring-rate regularization.

    This is a compact reproducible proxy for experiments that regularize
    generated event/censoring behavior at the marginal rate level. More
    granular conditional regularization can be plugged in without changing
    the training API.
    """
    p = real_event_rate.clamp(eps, 1 - eps)
    q = fake_event_rate.clamp(eps, 1 - eps)
    return p * torch.log(p / q) + (1 - p) * torch.log((1 - p) / (1 - q))
