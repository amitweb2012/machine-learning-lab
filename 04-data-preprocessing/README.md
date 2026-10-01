# 🧹 Data Preprocessing for Machine Learning

This section turns the EDA findings from `03-data-analysis` into a reproducible preprocessing workflow.

The existing insurance project is preserved **without changing its code**. The preprocessing examples are separate learning programs that use the same ideas and can be applied to the insurance dataset.

## Workflow

```text
Raw Insurance Data → Missing Values → Duplicates → Outliers
→ Encoding → Scaling → Feature Engineering → Train/Test Split
→ Pipeline → Machine Learning
```

## Programs

| # | Topic | Program |
|---|---|---|
| 1 | Missing values | `01_missing_values.py` |
| 2 | Duplicates | `02_duplicates.py` |
| 3 | Outlier treatment | `03_outlier_treatment.py` |
| 4 | Encoding | `04_encoding.py` |
| 5 | Feature scaling | `05_feature_scaling.py` |
| 6 | Normalization | `06_normalization.py` |
| 7 | Train/test split | `07_train_test_split.py` |
| 8 | Feature engineering | `08_feature_engineering.py` |
| 9 | Complete pipeline | `09_preprocessing_pipeline.py` |

## Insurance project

The existing insurance EDA project remains unchanged. These programs demonstrate preprocessing independently so the original analysis stays intact.

## Run

```bash
pip install -r requirements.txt
python 04-data-preprocessing/01_missing_values.py
python 04-data-preprocessing/02_duplicates.py
python 04-data-preprocessing/03_outlier_treatment.py
python 04-data-preprocessing/04_encoding.py
python 04-data-preprocessing/05_feature_scaling.py
python 04-data-preprocessing/06_normalization.py
python 04-data-preprocessing/07_train_test_split.py
python 04-data-preprocessing/08_feature_engineering.py
python 04-data-preprocessing/09_preprocessing_pipeline.py
```

## Key principle

Preprocessing should be reproducible and, for learned transformations, fitted only on training data to reduce data leakage.
