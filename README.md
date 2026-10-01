# 🧠 Machine Learning Lab

> **A portfolio-grade Machine Learning repository covering the complete journey from data analysis and statistics to model development, evaluation, MLOps, and deployment.**

[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![CI](https://github.com/amitweb2012/machine-learning-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/amitweb2012/machine-learning-lab/actions/workflows/ci.yml)

---

## 🎯 About This Repository

**Machine Learning Lab** is a structured learning and portfolio repository designed to demonstrate practical Machine Learning engineering skills.

It connects:

**Mathematics & Statistics → Data Analysis → Feature Engineering → Machine Learning → Evaluation → MLOps → Deployment**

The repository is intentionally organized so that every topic can evolve from a learning example into a production-style implementation.

---

## 🗺️ Learning & Project Roadmap

| Area | What you will find |
|---|---|
| 🐍 Python | NumPy, Pandas, functions, OOP, modules |
| 📐 Statistics | Probability, distributions, variance, correlation |
| 🧪 Statistical Testing | Z-test, t-test, chi-square, ANOVA, confidence intervals |
| 📊 EDA | Data quality, distributions, relationships, outliers |
| ⚙️ Preprocessing | Missing values, encoding, scaling, transformation |
| 🧬 Feature Engineering | Selection, creation, dimensionality reduction |
| 🤖 Supervised ML | Regression and classification algorithms |
| 🔍 Unsupervised ML | Clustering, PCA, anomaly detection |
| 🌳 Ensemble Learning | Random Forest, Gradient Boosting, XGBoost, LightGBM |
| 📈 Evaluation | Cross-validation, metrics, calibration, error analysis |
| 🔬 Explainability | Feature importance, SHAP, model interpretation |
| 🧩 ML Pipelines | Reproducible preprocessing and training pipelines |
| 🚀 MLOps | Experiment tracking, model versioning, CI |
| 🐳 Deployment | FastAPI, Docker, cloud-ready services |

---

## 📁 Repository Structure

```text
machine-learning-lab/
│
├── 01-python-foundation/
├── 02-statistics/
├── 03-data-analysis/
├── 04-data-preprocessing/
├── 05-supervised-learning/
├── 06-unsupervised-learning/
├── 07-ensemble-learning/
├── 08-model-evaluation/
├── 09-ml-projects/
│   ├── insurance-cost-prediction/
│   ├── house-price-prediction/
│   ├── customer-churn/
│   └── fraud-detection/
├── 10-ml-pipelines/
├── 11-deployment/
│
├── docs/
│   ├── roadmap.md
│   ├── algorithms.md
│   ├── statistics-formulas.md
│   └── interview-questions.md
│
├── assets/
│   ├── diagrams/
│   └── logo/
│
├── tests/
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── pyproject.toml
└── requirements.txt
```

---

## 🧠 Core Machine Learning Workflow

```text
                 ┌───────────────────┐
                 │   Business Goal   │
                 └─────────┬─────────┘
                           ↓
                 ┌───────────────────┐
                 │   Collect Data    │
                 └─────────┬─────────┘
                           ↓
                 ┌───────────────────┐
                 │   EDA & Quality   │
                 └─────────┬─────────┘
                           ↓
                 ┌───────────────────┐
                 │ Preprocessing &   │
                 │ Feature Engineering│
                 └─────────┬─────────┘
                           ↓
                 ┌───────────────────┐
                 │ Train / Validate  │
                 └─────────┬─────────┘
                           ↓
                 ┌───────────────────┐
                 │ Evaluate & Tune   │
                 └─────────┬─────────┘
                           ↓
                 ┌───────────────────┐
                 │ Explain & Package │
                 └─────────┬─────────┘
                           ↓
                 ┌───────────────────┐
                 │ Deploy & Monitor  │
                 └───────────────────┘
```

---

## ⭐ Portfolio Projects

### 1. Insurance Cost Prediction
End-to-end regression project covering:
- Data understanding and data quality
- Exploratory Data Analysis
- Feature relationships
- Categorical encoding
- Train/test split
- Regression models
- Metrics and residual analysis
- Reproducible ML pipeline

Path: [09-ml-projects/insurance-cost-prediction](09-ml-projects/insurance-cost-prediction/)

### 2. House Price Prediction
A regression workflow focused on:
- Missing-value treatment
- Feature engineering
- Numerical/categorical preprocessing
- Model comparison
- Cross-validation

### 3. Customer Churn Prediction
A classification project focused on:
- Class imbalance
- Precision, recall and F1
- ROC-AUC / PR-AUC
- Threshold analysis
- Explainability

### 4. Fraud Detection
A production-oriented classification problem focused on:
- Imbalanced data
- Leakage prevention
- Model evaluation
- Business-oriented error analysis

---

## 🧰 Technology Stack

**Languages**
- Python

**Data**
- NumPy
- Pandas
- Matplotlib
- Seaborn

**Machine Learning**
- scikit-learn
- XGBoost
- LightGBM

**Experimentation / MLOps**
- MLflow
- Joblib
- pytest
- GitHub Actions

**Deployment**
- FastAPI
- Docker
- Cloud-ready architecture

---

## 🚀 Getting Started

### Clone

```bash
git clone https://github.com/amitweb2012/machine-learning-lab.git
cd machine-learning-lab
```

### Create environment

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run tests

```bash
pytest
```

---

## 📚 Documentation

- [Machine Learning Roadmap](docs/roadmap.md)
- [Algorithms Reference](docs/algorithms.md)
- [Statistics Formula Sheet](docs/statistics-formulas.md)
- [ML Interview Questions](docs/interview-questions.md)
- [Project Template](09-ml-projects/PROJECT_TEMPLATE.md)

---

## 💼 Portfolio Positioning

This repository is designed to demonstrate more than algorithm knowledge.

It emphasizes:

**Problem Definition → Data Understanding → Statistical Reasoning → Feature Engineering → Modeling → Evaluation → Reproducibility → Deployment**

That makes each project suitable for discussion in technical interviews and portfolio reviews.

---

## 🧑‍💻 Author

**Amit Das**

GitHub: [@amitweb2012](https://github.com/amitweb2012)

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
