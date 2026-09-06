# Source Code

This directory contains the core implementation of EndSurvGAN.

Recommended organization:

```text
src/
├── models/        # Generator and discriminator architectures
├── losses/        # Survival-aware and adversarial objectives
├── training/      # Training pipeline and optimization
└── evaluation/    # Survival metrics and validation utilities
```

The implementation follows a modular design to support reproducible survival modeling experiments.
