"""Core neural modules for EndSurvGAN.

This module follows the architecture described in the project summary:
a fully connected generator and discriminator operating on joint survival
samples (X, T, delta). It intentionally keeps preprocessing and dataset-
specific encoding outside the model so experiments can remain reproducible.
"""

from __future__ import annotations

import torch
from torch import nn


class Generator(nn.Module):
    """Generate synthetic joint survival samples (X*, T*, delta*).

    Parameters
    ----------
    latent_dim:
        Dimension of the latent noise vector.
    n_covariates:
        Number of generated covariates.
    hidden_dim:
        Width of each hidden layer.
    """

    def __init__(self, latent_dim: int, n_covariates: int, hidden_dim: int = 256):
        super().__init__()
        self.n_covariates = n_covariates
        out_dim = n_covariates + 2  # covariates + time + event logit

        self.network = nn.Sequential(
            nn.Linear(latent_dim, hidden_dim),
            nn.LeakyReLU(0.2),
            nn.Linear(hidden_dim, hidden_dim),
            nn.LeakyReLU(0.2),
            nn.Linear(hidden_dim, hidden_dim),
            nn.LeakyReLU(0.2),
            nn.Linear(hidden_dim, out_dim),
        )

    def forward(self, z: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        raw = self.network(z)
        x = raw[:, : self.n_covariates]
        # Positive observed time. softplus avoids negative generated times.
        t = torch.nn.functional.softplus(raw[:, self.n_covariates : self.n_covariates + 1])
        # Probability form for the event indicator during training.
        delta_prob = torch.sigmoid(raw[:, self.n_covariates + 1 :])
        return x, t, delta_prob


class Discriminator(nn.Module):
    """Wasserstein critic for real or synthetic survival samples."""

    def __init__(self, n_covariates: int, hidden_dim: int = 256):
        super().__init__()
        in_dim = n_covariates + 2
        self.network = nn.Sequential(
            nn.Linear(in_dim, hidden_dim),
            nn.LeakyReLU(0.2),
            nn.Linear(hidden_dim, hidden_dim),
            nn.LeakyReLU(0.2),
            nn.Linear(hidden_dim, hidden_dim),
            nn.LeakyReLU(0.2),
            nn.Linear(hidden_dim, 1),
        )

    def forward(self, x: torch.Tensor, t: torch.Tensor, delta: torch.Tensor) -> torch.Tensor:
        sample = torch.cat([x, t, delta], dim=1)
        return self.network(sample)


class EndSurvGAN(nn.Module):
    """Convenience wrapper bundling the generator and discriminator."""

    def __init__(self, latent_dim: int, n_covariates: int, hidden_dim: int = 256):
        super().__init__()
        self.generator = Generator(latent_dim, n_covariates, hidden_dim)
        self.discriminator = Discriminator(n_covariates, hidden_dim)
