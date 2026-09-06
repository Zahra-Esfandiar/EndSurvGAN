# Experiments 🧪

This directory contains experiment configurations, benchmark settings, and reproducible evaluation workflows.

## Planned Structure

```
experiments/
|
├── datasets/
├── configs/
├── training_runs/
├── evaluation/
└── reports/
```

## Benchmark Protocol

Recommended reporting:

| Category | Metrics |
|---|---|
| Synthetic Fidelity | Distribution comparison |
| Survival Preservation | Kaplan-Meier similarity |
| Predictive Utility | C-index |
| Robustness | Ablation analysis |

## Reproducibility Goals

Each experiment should document:

- Dataset source
- Preprocessing steps
- Hyperparameters
- Random seeds
- Evaluation metrics

