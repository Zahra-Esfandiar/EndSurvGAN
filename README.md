# 🧬 EndSurvGAN

<p align="center">
  <img src="https://img.shields.io/badge/Research-Survival%20Analysis-4B0082" />
  <img src="https://img.shields.io/badge/AI-Generative%20Modeling-2563EB" />
  <img src="https://img.shields.io/badge/Domain-Healthcare%20Data-0F766E" />
</p>

<h2 align="center">End-to-End Survival-Aware Generative Modeling of Censored Time-to-Event Data</h2>

<p align="center">
<b>Survival Analysis × Generative AI × Statistical Machine Learning</b>
</p>

---

## 🌟 Research Vision

Real-world healthcare datasets are often limited by privacy constraints, incomplete follow-up, and restricted accessibility. However, survival data contains complex structures that cannot be captured by conventional synthetic data generators.

**EndSurvGAN** introduces a survival-aware generative framework designed to create realistic synthetic censored time-to-event data while preserving essential survival characteristics.

The goal is not only realistic feature generation, but preservation of the underlying survival mechanism.

---

## 🎯 Problem Statement

Standard synthetic tabular generators often ignore the unique nature of survival datasets:

- ⏳ Time-to-event dependency
- 🚩 Event/censoring mechanisms
- 📈 Survival distributions
- 🧬 Predictor-event relationships

EndSurvGAN explicitly models these components through a unified probabilistic framework.

---

## 🧠 Core Idea

The framework learns the joint distribution:

$$
P(X,T,\Delta)
$$

where:

- **X** → patient-level covariates
- **T** → observed survival time
- **Δ** → event indicator

The generated synthetic data aims to maintain:

✅ Covariate distribution fidelity  
✅ Survival-time dynamics  
✅ Censoring behavior  
✅ Downstream survival prediction performance

---

# 🏗️ Model Architecture

```
Random Noise z
      |
      v
+-------------+
| Generator   |
+-------------+
      |
      v
Synthetic (X*, T*, Δ*)
      |
      v
+-----------------------+
| Survival Constraints  |
| Censoring Awareness   |
+-----------------------+
      |
      v
+-------------+
| Discriminator|
+-------------+
```

The architecture combines adversarial learning with survival-specific objectives.

---

# 🔬 Methodological Contributions

### Survival-Aware Generation

Models censored time-to-event data as a structured survival problem rather than ordinary tabular synthesis.

### Censoring-Aware Learning

Explicitly incorporates censoring information during training.

### Adversarial Optimization

Uses WGAN-GP inspired optimization for stable generative learning.

### Survival-Specific Evaluation

Evaluates whether synthetic data remains useful for downstream survival analysis.

---

# 📊 Experimental Evaluation

Benchmark datasets:

| Dataset | Samples | Features | Censoring |
|---|---:|---:|---:|
| SUPPORT | 9,105 | 14 | 32% |
| ACTG | 2,467 | 17 | 64% |
| Rotterdam | 2,982 | 7 | 57% |

Evaluation framework:

- Kaplan–Meier curve comparison
- Distributional similarity
- Survival prediction utility
- Concordance Index (C-index)
- Ablation studies

---

# ⚙️ Technical Stack

| Area | Tools |
|---|---|
| Language | Python |
| Deep Learning | PyTorch |
| Statistics | Survival Analysis |
| Modeling | Generative Neural Networks |
| Evaluation | Statistical Validation |

---

# 📁 Project Structure

```text
EndSurvGAN/
│
├── README.md
├── CITATION.cff
├── ARCHITECTURE.md
├── requirements.txt
│
├── src/
│   ├── models/
│   ├── losses/
│   ├── training/
│   └── evaluation/
│
├── experiments/
└── results/
```

---

# 📄 Research Status

**EndSurvGAN: End-to-End Survival-Aware Generative Modeling of Censored Time-to-Event Data**

📌 Submitted to the **18th Iranian Statistics Conference (2026)**  
🔄 Status: Under Review

---

# 🚀 Future Research Directions

- Competing-risk synthetic survival generation
- Recurrent event modeling
- Privacy-preserving healthcare AI
- Uncertainty-aware survival generation
- Integration with large-scale clinical datasets

---

# 👩‍🔬 Author

**Zahra Esfandiar**  
Statistics & Data Science Researcher

Research Interests:

🧬 Survival Analysis  
🏥 Biostatistics & Healthcare AI  
📊 Statistical Machine Learning  
🤖 Generative Modeling
