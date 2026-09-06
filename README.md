# 🧬 EndSurvGAN

<p align="center">
  <img src="https://img.shields.io/badge/Research-Survival%20Analysis-4B0082" />
  <img src="https://img.shields.io/badge/AI-Generative%20Modeling-2563EB" />
  <img src="https://img.shields.io/badge/Conference-Oral%20Presentation-0F766E" />
  <img src="https://img.shields.io/badge/Framework-PyTorch-EE4C2C" />
</p>

<h2 align="center">End-to-End Survival-Aware Generative Modeling of Censored Time-to-Event Data</h2>

<p align="center"><b>Survival Analysis × Generative AI × Statistical Machine Learning</b></p>

---

<p align="center">
<img src="assets/architecture.svg" width="750" />
</p>

---

## 🌟 Research Vision

EndSurvGAN is a survival-aware generative framework designed to generate realistic synthetic censored time-to-event data while preserving essential survival structures.

Unlike conventional tabular data generators, EndSurvGAN explicitly models:

- Covariate distributions
- Survival-time dynamics
- Event/censoring mechanisms
- Predictor–outcome relationships
- Downstream survival modeling utility

The project aims to support privacy-aware and reproducible healthcare analytics through statistically grounded synthetic survival data generation.

---

## 🎤 Research Recognition

🏆 **Accepted as an Oral Presentation** at the **18th Iranian Statistics Conference (2026)**

**Presentation:** *EndSurvGAN: End-to-End Survival-Aware Generative Modeling of Censored Time-to-Event Data*

### 📄 Conference Material

- [`Conference Summary PDF`](paper/Summary-Isc18ZahraEsfandiar.pdf)
- [`Paper Materials`](paper/README.md)

---

## 🧠 Core Idea

The framework learns the joint survival distribution:

$$P(X,T,\Delta)$$

where:

- **X** → patient-level covariates
- **T** → observed survival time
- **Δ** → event indicator

The research objective combines adversarial learning with survival-aware and censoring-aware regularization:

$$L_{total}=L_{adv}+\lambda_{surv}L_{surv}+\lambda_{cens}L_{cens}$$

with WGAN-GP optimization for adversarial stability.

---

## ⚡ Quick Start

```bash
git clone https://github.com/Zahra-Esfandiar/EndSurvGAN.git
cd EndSurvGAN
pip install -r requirements.txt
jupyter notebook notebooks/01_EndSurvGAN_demo.ipynb
```

The demo notebook provides a minimal model forward pass and loads the reported benchmark/ablation tables. Full conference reproduction additionally requires the original benchmark preprocessing and experiment configuration.

See [`QUICKSTART.md`](QUICKSTART.md) for the workflow.

---

## 🏗️ Research Implementation

The repository now includes executable research scaffolding aligned with the documented EndSurvGAN design:

```text
src/
├── models/
│   └── end_surv_gan.py
├── losses/
│   └── survival_losses.py
├── training/
│   └── train.py
└── evaluation/
    └── metrics.py
```

Implemented components include:

- Fully connected Generator and Discriminator
- WGAN critic/generator objectives
- Gradient penalty
- Censoring-rate KL regularization utility
- Reproducible training configuration
- Kaplan–Meier distance evaluation
- Distributional diagnostic helpers

---

## 📊 Experimental Evaluation

Benchmark datasets:

| Dataset | Samples | Features | Censoring Rate |
|---|---:|---:|---:|
| SUPPORT | 9,105 | 14 | 32% |
| ACTG | 2,467 | 17 | 64% |
| Rotterdam | 2,982 | 7 | 57% |

### Reported benchmark results

| Dataset | Method | KS/JS ↓ | KM-Distance ↓ | C-index ↑ |
|---|---|---:|---:|---:|
| SUPPORT | SurvivalGAN | 0.101 | 0.086 | 0.68 |
| SUPPORT | **EndSurvGAN** | **0.082** | **0.061** | **0.71** |
| ACTG | SurvivalGAN | 0.095 | 0.081 | 0.69 |
| ACTG | **EndSurvGAN** | **0.078** | **0.058** | **0.72** |
| Rotterdam | SurvivalGAN | 0.097 | 0.079 | 0.71 |
| Rotterdam | **EndSurvGAN** | **0.081** | **0.063** | **0.74** |

Machine-readable results: [`results/benchmark_results.csv`](results/benchmark_results.csv)

### Ablation study

| Variant | C-index |
|---|---:|
| Two-Stage Generator | 0.67 |
| EndSurvGAN without Censoring Loss | 0.69 |
| EndSurvGAN without Survival Loss | 0.68 |
| **Full EndSurvGAN** | **0.71** |

Machine-readable results: [`results/ablation_results.csv`](results/ablation_results.csv)

---

## 🧪 Evaluation Framework

The study evaluates synthetic survival data using:

- Kaplan–Meier curve alignment
- Distributional fidelity
- Survival prediction utility
- Concordance Index (C-index)
- Ablation analysis

The current repository includes reusable evaluation helpers in [`src/evaluation/metrics.py`](src/evaluation/metrics.py).

---

## 📚 Research Documentation

- 🏗️ [`ARCHITECTURE.md`](docs/ARCHITECTURE.md) — model design
- 🔄 [`MODEL_PIPELINE.md`](docs/MODEL_PIPELINE.md) — end-to-end workflow
- 🧠 [`RESEARCH_NOTES.md`](docs/RESEARCH_NOTES.md) — research framing
- 📖 [`RELATED_WORK.md`](docs/RELATED_WORK.md) — methodological context
- 🎤 [`CONFERENCE_PRESENTATION.md`](docs/CONFERENCE_PRESENTATION.md) — conference record
- 🎓 [`ACADEMIC_IMPACT.md`](docs/ACADEMIC_IMPACT.md) — research significance
- 📚 [`HOW_TO_CITE.md`](docs/HOW_TO_CITE.md) — citation guidance
- 🗺️ [`ROADMAP.md`](ROADMAP.md) — planned extensions

---

## 📁 Repository Structure

```text
EndSurvGAN/
├── README.md
├── QUICKSTART.md
├── CITATION.cff
├── requirements.txt
├── ROADMAP.md
├── assets/
│   └── architecture.svg
├── docs/
├── experiments/
├── notebooks/
│   └── 01_EndSurvGAN_demo.ipynb
├── paper/
│   ├── README.md
│   └── Summary-Isc18ZahraEsfandiar.pdf
├── results/
│   ├── benchmark_results.csv
│   └── ablation_results.csv
└── src/
    ├── models/
    ├── losses/
    ├── training/
    └── evaluation/
```

---

## ⚙️ Technical Stack

**Python · PyTorch · Survival Analysis · Statistical Machine Learning · Generative Modeling · Reproducible Research**

---

## 🔭 Future Directions

- Competing-risk survival generation
- Recurrent-event modeling
- Privacy-preserving synthetic healthcare data
- Uncertainty-aware survival modeling
- Larger-scale clinical and biomedical validation

---

## 👩‍🔬 Author

**Zahra Esfandiar**  
Statistics & Data Science Researcher

**Research interests:** Survival Analysis · Biostatistics · Statistical Machine Learning · Healthcare AI · Generative Modeling
