# 🧬 EndSurvGAN

<p align="center">
  <b>End-to-End Survival-Aware Generative Modeling of Censored Time-to-Event Data</b>
</p>

<p align="center">
  Survival Analysis × Generative AI × Statistical Learning
</p>

---

## 📌 Overview

**EndSurvGAN** is an end-to-end survival-aware generative framework designed to generate realistic synthetic censored time-to-event datasets while preserving important survival-specific structures.

Unlike conventional tabular data generators that treat survival time and censoring indicators as ordinary variables, EndSurvGAN explicitly models the joint survival distribution and aims to preserve:

- Covariate distributions
- Survival-time dynamics
- Censoring mechanisms
- Relationships between predictors and event times
- Downstream predictive utility for survival models

The project addresses a key challenge in biomedical and healthcare research: enabling privacy-aware data sharing and reproducible survival modeling when real patient-level datasets are limited.

---

## 🎯 Research Motivation

Survival datasets contain unique characteristics beyond standard tabular data:

- Observed survival times
- Event indicators
- Right censoring mechanisms
- Time-to-event dependencies

A useful synthetic survival generator should preserve these structures rather than simply generate realistic-looking feature values.

EndSurvGAN was developed to provide a unified survival-aware generative modeling approach.

---

## 🧠 Methodology

EndSurvGAN learns the joint distribution:

\[
P(X,T,\Delta)
\]

where:

- **X** represents patient covariates
- **T** represents observed survival time
- **Δ** represents event/censoring indicator

The framework uses an adversarial learning architecture consisting of:

### Generator
Generates synthetic survival samples:

\[
G(z)=(X^*,T^*,\Delta^*)
\]

### Discriminator
Distinguishes real survival observations from generated samples.

---

## 🏗️ Model Contributions

Key methodological components:

✅ Survival-aware generative modeling  
✅ Censoring-aware regularization  
✅ WGAN-GP adversarial optimization  
✅ Joint modeling of covariates, survival time, and censoring behavior  
✅ Survival-specific evaluation framework

---

## 📊 Evaluation Framework

EndSurvGAN is evaluated using benchmark survival datasets:

| Dataset | Samples | Features | Censoring Rate |
|---|---:|---:|---:|
| SUPPORT | 9,105 | 14 | 32% |
| ACTG | 2,467 | 17 | 64% |
| Rotterdam | 2,982 | 7 | 57% |

Evaluation metrics include:

- Distributional fidelity
- Kaplan–Meier curve alignment
- Survival model predictive utility
- Concordance Index (C-index)
- Ablation analysis

---

## 🔬 Technical Implementation

Implemented using:

- Python
- PyTorch
- Deep Neural Networks
- Statistical Survival Analysis
- Computational Statistics

The implementation includes:

- Generator and discriminator architectures
- Custom survival-aware loss functions
- Training pipeline
- Validation pipeline
- Survival-specific evaluation tools

---

## 📄 Research Publication Status

**EndSurvGAN: End-to-End Survival-Aware Generative Modeling of Censored Time-to-Event Data**

📌 Submitted to the **18th Iranian Statistics Conference (2026)**  
🔄 Status: Under Review

---

## 🚀 Future Directions

Potential extensions include:

- Competing-risk survival generation
- Recurrent-event modeling
- Privacy-preserving synthetic healthcare data
- Uncertainty-aware survival modeling

---

## 👩‍🔬 Author

**Zahra Esfandiar**  
Statistics & Data Science Researcher

Research interests:

- Survival Analysis
- Biostatistics
- Statistical Machine Learning
- Healthcare AI
- Generative Modeling
