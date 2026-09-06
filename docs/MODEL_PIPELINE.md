# EndSurvGAN Model Pipeline 🧬

## High-Level Workflow

```
Clinical Survival Dataset
          |
          v
Data Representation
(X, T, Δ)
          |
          v
Survival-Aware Generator
          |
          v
Synthetic Survival Samples
          |
          v
Survival Constraints + Regularization
          |
          v
Adversarial Discriminator
          |
          v
Quality Assessment
(KM Curves, Fidelity, C-index)
```

## Core Components

### Generator
Learns to generate synthetic observations containing:
- Covariates (X)
- Time-to-event information (T)
- Event indicator (Δ)

### Discriminator
Evaluates whether generated samples preserve survival characteristics of the original data.

### Evaluation Layer
Measures:
- Distributional similarity
- Survival curve preservation
- Predictive utility
- Model robustness

## Research Goal

The goal is not only realistic synthetic tabular generation, but preservation of survival mechanisms required for reliable downstream biomedical modeling.
