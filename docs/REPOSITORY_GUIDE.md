# 🧬 EndSurvGAN Repository Guide

This guide explains how the repository is organized for research use.

## Research Flow

```
Clinical Survival Data
        ↓
Data Representation (X, T, Δ)
        ↓
Survival-Aware Generative Modeling
        ↓
Synthetic Time-to-Event Data
        ↓
Evaluation & Validation
```

## Main Components

### `src/`
Core implementation modules:

- `models/` — model architectures
- `losses/` — optimization objectives
- `training/` — training workflows
- `evaluation/` — survival evaluation utilities

### `experiments/`
Research experiment organization:

- configurations
- benchmark settings
- reproducibility notes

### `results/`
Reported experimental outputs:

- benchmark comparisons
- ablation studies
- evaluation summaries

### `paper/`
Conference and research materials:

- conference summary
- supplementary documents

## Recommended Usage

1. Read the main `README.md`.
2. Review the architecture documentation.
3. Check the quick start workflow.
4. Run experiments with documented configurations.
5. Compare results using the evaluation framework.

## Research Identity

EndSurvGAN connects:

- Survival Analysis
- Biostatistics
- Statistical Machine Learning
- Generative AI
- Healthcare Data Science
