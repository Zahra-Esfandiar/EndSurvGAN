# EndSurvGAN Research Notes

## Research Theme

EndSurvGAN explores survival-aware generative modeling for censored time-to-event data.

## Scientific Questions

- How can synthetic survival datasets preserve time-to-event structure?
- How can censoring mechanisms be modeled instead of ignored?
- How can generated data maintain downstream survival prediction utility?

## Key Components

### Data Representation

The framework considers:

- Covariates (X)
- Survival time (T)
- Event indicator (Δ)

### Evaluation Philosophy

Synthetic data quality should be assessed beyond feature similarity by considering survival-specific properties:

- Kaplan–Meier curve preservation
- Predictive utility
- Distributional fidelity
- Survival consistency

## Future Research Extensions

- Competing risks generation
- Recurrent event survival modeling
- Differential privacy integration
- Uncertainty-aware synthetic survival modeling
