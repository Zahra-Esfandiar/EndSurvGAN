# 🧬 EndSurvGAN

<h2 align="center">End-to-End Survival-Aware Generative Modeling of Censored Time-to-Event Data</h2>

<p align="center"><b>Survival Analysis × Generative AI × Statistical Machine Learning</b></p>

---

## 🌟 Research Vision

EndSurvGAN is a survival-aware generative framework for generating realistic synthetic censored time-to-event data while preserving survival-specific structures.

Unlike conventional tabular generators, EndSurvGAN explicitly considers:

- Covariate distributions
- Survival-time dynamics
- Event/censoring mechanisms
- Relationships between predictors and outcomes
- Downstream survival modeling utility

The project focuses on privacy-aware and reproducible healthcare analytics using synthetic survival data.

---

## 🧠 Core Idea

The framework models the joint survival distribution:

$$P(X,T,\Delta)$$

where:

- **X**: patient covariates
- **T**: survival time
- **Δ**: event indicator

---

## 🏗️ Model Overview

```
Random Noise z
      |
      v
 Generator Network
      |
      v
Synthetic Survival Data
      |
      v
Survival-aware Constraints
      |
      v
Discriminator Network
```

Key components:

✅ Survival-aware generation  
✅ Censoring-aware learning  
✅ WGAN-GP optimization  
✅ Survival-specific evaluation

---

## 📊 Evaluation Framework

Benchmark datasets:

| Dataset | Samples | Features |
|---|---:|---:|
| SUPPORT | 9,105 | 14 |
| ACTG | 2,467 | 17 |
| Rotterdam | 2,982 | 7 |

Evaluation includes:

- Kaplan–Meier curve alignment
- Distributional fidelity
- Survival prediction utility
- Concordance Index (C-index)
- Ablation analysis

---

## 📄 Research Presentation

**EndSurvGAN: End-to-End Survival-Aware Generative Modeling of Censored Time-to-Event Data**

📌 Accepted as an **Oral Presentation** at the **18th Iranian Statistics Conference (2026)** 🎤

The work presents a survival-aware generative approach for synthetic censored time-to-event data and its applications in statistical learning and healthcare analytics.

---

## ⚙️ Technical Stack

- Python
- PyTorch
- Deep Neural Networks
- Survival Analysis
- Statistical Machine Learning

---

## 🚀 Future Directions

- Competing-risk survival generation
- Recurrent-event modeling
- Privacy-preserving healthcare AI
- Uncertainty-aware survival modeling

---

## 👩‍🔬 Author

**Zahra Esfandiar**  
Statistics & Data Science Researcher

Research Interests:

🧬 Survival Analysis  
🏥 Biostatistics & Healthcare AI  
📊 Statistical Machine Learning  
🤖 Generative Modeling
