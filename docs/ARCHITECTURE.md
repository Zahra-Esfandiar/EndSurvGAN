# EndSurvGAN Architecture

## Overview

EndSurvGAN is a survival-aware generative framework designed for censored time-to-event data. The framework aims to generate synthetic survival datasets while preserving important statistical characteristics of survival outcomes and censoring mechanisms.

## High-Level Pipeline

```text
Original Survival Dataset
          |
          v
Data Preprocessing
          |
          v
Generator Network  <---- Survival-aware Objectives
          |
          v
Synthetic Survival Data
          |
          v
Discriminator + Evaluation
          |
          v
Quality Assessment
```

## Core Components

### Generator
Learns the underlying structure of survival data and generates synthetic samples.

### Discriminator
Evaluates realism of generated samples through adversarial learning.

### Survival-aware Constraints
The model incorporates survival-specific objectives to maintain:

- Time-to-event distributions
- Censoring behavior
- Covariate relationships
- Downstream predictive utility

## Evaluation

Recommended evaluation includes:

- Kaplan-Meier curve comparison
- Distributional similarity
- Survival prediction performance
- C-index evaluation
