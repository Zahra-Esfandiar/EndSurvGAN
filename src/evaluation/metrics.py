"""Evaluation helpers for synthetic survival data."""

from __future__ import annotations

import numpy as np
import pandas as pd
from lifelines import KaplanMeierFitter


def km_curve(time, event, timeline=None):
    """Return a Kaplan–Meier survival curve as a pandas Series."""
    kmf = KaplanMeierFitter()
    kmf.fit(np.asarray(time), event_observed=np.asarray(event))
    if timeline is None:
        return kmf.survival_function_["KM_estimate"]
    return kmf.predict(timeline)


def km_distance(real_time, real_event, fake_time, fake_event, n_grid: int = 200) -> float:
    """Mean absolute distance between real and synthetic KM curves."""
    max_time = min(np.max(real_time), np.max(fake_time))
    grid = np.linspace(0.0, float(max_time), n_grid)
    real_curve = np.asarray(km_curve(real_time, real_event, grid), dtype=float)
    fake_curve = np.asarray(km_curve(fake_time, fake_event, grid), dtype=float)
    return float(np.mean(np.abs(real_curve - fake_curve)))


def marginal_fidelity(real_x, fake_x) -> pd.DataFrame:
    """Simple per-feature summary for quick distributional checks.

    The conference evaluation uses broader distributional fidelity metrics;
    this helper provides a transparent first-pass diagnostic for notebooks.
    """
    real = pd.DataFrame(real_x)
    fake = pd.DataFrame(fake_x)
    rows = []
    for col in real.columns:
        rows.append(
            {
                "feature": str(col),
                "real_mean": float(real[col].mean()),
                "synthetic_mean": float(fake[col].mean()),
                "real_std": float(real[col].std()),
                "synthetic_std": float(fake[col].std()),
            }
        )
    return pd.DataFrame(rows)
