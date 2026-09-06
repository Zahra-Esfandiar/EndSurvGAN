# 🚀 EndSurvGAN Quick Start

## Overview

This guide describes the intended workflow for reproducing EndSurvGAN experiments.

## Pipeline

1. Prepare survival dataset
2. Define covariates (X), survival time (T), and event indicator (Δ)
3. Configure training parameters
4. Train the survival-aware generative model
5. Evaluate synthetic data quality

## Evaluation

Recommended evaluation includes:

- Survival distribution comparison
- Kaplan–Meier curve alignment
- Distributional fidelity
- Downstream survival prediction utility
- Ablation studies

## Reproducibility

Experiments should record:

- Dataset configuration
- Random seed
- Model hyperparameters
- Evaluation metrics
