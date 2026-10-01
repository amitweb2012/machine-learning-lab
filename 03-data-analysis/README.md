# 📊 Data Analysis & EDA

This section builds the practical bridge between **Statistics** and **Machine Learning**.

The goal of Exploratory Data Analysis (EDA) is to understand the structure, quality, distributions, relationships, and limitations of data before modeling.

## EDA workflow

```text
Load Data → Understand Structure → Data Quality → Univariate Analysis
→ Bivariate Analysis → Outliers → Correlation → Interpretation → ML
```

## Programs

| Topic | Program |
|---|---|
| Dataset overview | `01_dataset_overview.py` |
| Data quality | `02_data_quality.py` |
| Univariate analysis | `03_univariate_analysis.py` |
| Categorical analysis | `04_categorical_analysis.py` |
| Bivariate analysis | `05_bivariate_analysis.py` |
| Outlier analysis | `06_outlier_analysis.py` |
| Correlation analysis | `07_correlation_analysis.py` |
| Distribution analysis | `08_distribution_analysis.py` |
| Complete EDA | `09_complete_eda.py` |

## Mathematical concepts

### Mean

**x̄ = Σxᵢ / n**

Describes the arithmetic center of numerical observations.

### Median

The middle observation after sorting. It is generally less sensitive to extreme observations than the mean.

### Variance

**σ² = Σ(xᵢ − μ)² / N**

Measures squared spread around the population mean.

### Standard deviation

**σ = √σ²**

Measures spread in the original units.

### Z-score

**z = (x − μ) / σ**

Measures distance from the mean in standard-deviation units.

### Five-number summary

**Minimum, Q1, Median, Q3, Maximum**

The interquartile range is **IQR = Q3 − Q1**.

A common potential-outlier rule is **x < Q1 − 1.5(IQR)** or **x > Q3 + 1.5(IQR)**.

### Covariance

**Cov(X,Y) = Σ[(xᵢ − x̄)(yᵢ − ȳ)] / (n − 1)**

Shows the direction of joint variation.

### Pearson correlation

**r = Cov(X,Y) / (σₓσᵧ)**

Measures the strength and direction of a linear relationship from -1 to +1.

> Correlation is association, not proof of causation.

## Visualization guide

- **Histogram** → distribution of a numerical variable
- **Box plot** → spread, quartiles and potential outliers
- **Bar chart** → compare categories
- **Scatter plot** → relationship between two numerical variables
- **Heatmap** → inspect a correlation matrix

## Dataset

The programs use a small reproducible synthetic customer dataset, keeping the EDA project self-contained. It includes numerical and categorical features such as age, annual income, monthly spend, tenure, support tickets, satisfaction, plan, region, and churn.

The workflow can be adapted to a CSV with `pd.read_csv(...)`.

## Run

```bash
pip install -r requirements.txt

python 03-data-analysis/01_dataset_overview.py
python 03-data-analysis/02_data_quality.py
python 03-data-analysis/03_univariate_analysis.py
python 03-data-analysis/04_categorical_analysis.py
python 03-data-analysis/05_bivariate_analysis.py
python 03-data-analysis/06_outlier_analysis.py
python 03-data-analysis/07_correlation_analysis.py
python 03-data-analysis/08_distribution_analysis.py
python 03-data-analysis/09_complete_eda.py
```

Visualizations are saved under `03-data-analysis/output/`.

## Connection to Machine Learning

EDA helps determine what preprocessing and modeling work may be appropriate: missing-value treatment, encoding, scaling, transformation, feature engineering, leakage checks, and model evaluation strategy.

EDA is an evidence-discovery stage. Observed association does not by itself establish causation.
