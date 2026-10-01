"""
Insurance Dataset - Exploratory Data Analysis (EDA)

Learning project:
    Load Dataset
        ↓
    Understand Data
        ↓
    Data Quality
        ↓
    Univariate EDA
        ↓
    Bivariate EDA
        ↓
    Feature Engineering
        ↓
    Statistical Analysis

This file intentionally stops at EDA/statistical analysis.
Model training and model evaluation are NOT included yet.
"""

import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import chi2_contingency, pearsonr

warnings.filterwarnings("ignore")

# ---------------------------------------------------------------------------
# 1. LOAD DATASET
# ---------------------------------------------------------------------------

DATA_FILE = "insurance.csv"

df = pd.read_csv(DATA_FILE)

print("\n" + "=" * 80)
print("1. LOAD DATASET")
print("=" * 80)
print(f"Dataset loaded from: {DATA_FILE}")
print(f"Shape: {df.shape}")


# ---------------------------------------------------------------------------
# 2. UNDERSTAND DATA
# ---------------------------------------------------------------------------

print("\n" + "=" * 80)
print("2. UNDERSTAND DATA")
print("=" * 80)

print("\n--- First 5 rows ---")
print(df.head())

print("\n--- Last 5 rows ---")
print(df.tail())

print("\n--- Dataset shape ---")
print(df.shape)

print("\n--- Dataset information ---")
df.info()

print("\n--- Descriptive statistics ---")
print(df.describe())

print("\n--- Column names ---")
print(df.columns.tolist())

print("\n--- Data types ---")
print(df.dtypes)


# ---------------------------------------------------------------------------
# 3. DATA QUALITY
# ---------------------------------------------------------------------------

print("\n" + "=" * 80)
print("3. DATA QUALITY")
print("=" * 80)

# 3.1 Missing values
print("\n--- Missing values ---")
missing_values = df.isnull().sum()
print(missing_values)

print("\n--- Missing-value percentage ---")
missing_percentage = (df.isnull().mean() * 100).round(2)
print(missing_percentage)

# 3.2 Duplicate rows
print("\n--- Duplicate rows ---")
duplicate_count = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicate_count}")

# Create a cleaned copy for the remaining EDA work.
# We remove exact duplicate rows and rows containing missing values.
df_cleaned = df.copy()
df_cleaned.drop_duplicates(inplace=True) # remove exact duplicate rows
df_cleaned.dropna(inplace=True)  # drop rows with missing values

print("\n--- Shape after basic cleaning ---")
print(df_cleaned.shape)

print("\n--- Missing values after cleaning ---")
print(df_cleaned.isnull().sum())

print("\n--- Duplicate rows after cleaning ---")
print(df_cleaned.duplicated().sum())


# ---------------------------------------------------------------------------
# 4. IDENTIFY NUMERICAL AND CATEGORICAL FEATURES
# ---------------------------------------------------------------------------

print("\n" + "=" * 80)
print("4. NUMERICAL AND CATEGORICAL FEATURES")
print("=" * 80)

numeric_columns = ["age", "bmi", "children", "charges"]
categorical_columns = ["sex", "smoker", "region"]

print("\nNumerical columns:")
print(numeric_columns)

print("\nCategorical columns:")
print(categorical_columns)


# ---------------------------------------------------------------------------
# 5. UNIVARIATE EDA - NUMERICAL FEATURES
# UNIVARIATE EDA focuses on analyzing each feature individually to understand 
# its distribution, central tendency, and spread. For numerical features, 
# we can use histograms, boxplots, and descriptive statistics.
# ---------------------------------------------------------------------------

print("\n" + "=" * 80)
print("5. UNIVARIATE EDA - NUMERICAL FEATURES")
print("=" * 80)

# Histograms show the distribution of each numerical variable.
for col in numeric_columns:
    plt.figure(figsize=(8, 4))
    sns.histplot(data=df_cleaned, x=col, kde=True)
    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

# Boxplots help identify median, spread, and potential outliers.
for col in numeric_columns:
    plt.figure(figsize=(8, 3))
    sns.boxplot(data=df_cleaned, x=col)
    plt.title(f"Boxplot of {col}")
    plt.xlabel(col)
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------------------
# 6. UNIVARIATE EDA - CATEGORICAL FEATURES
# ---------------------------------------------------------------------------

print("\n" + "=" * 80)
print("6. UNIVARIATE EDA - CATEGORICAL FEATURES")
print("=" * 80)

for col in categorical_columns:
    print(f"\n--- Value counts for {col} ---")
    print(df_cleaned[col].value_counts())

    plt.figure(figsize=(8, 4))
    sns.countplot(data=df_cleaned, x=col)
    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------------------
# 7. FIVE-NUMBER SUMMARY AND IQR
# ---------------------------------------------------------------------------

print("\n" + "=" * 80)
print("7. FIVE-NUMBER SUMMARY AND IQR")
print("=" * 80)

for col in numeric_columns:
    minimum = df_cleaned[col].min()
    q1 = df_cleaned[col].quantile(0.25)
    median = df_cleaned[col].median()
    q3 = df_cleaned[col].quantile(0.75)
    maximum = df_cleaned[col].max()
    iqr = q3 - q1

    print(f"\n--- {col} ---")
    print(f"Minimum : {minimum}")
    print(f"Q1      : {q1}")
    print(f"Median  : {median}")
    print(f"Q3      : {q3}")
    print(f"Maximum : {maximum}")
    print(f"IQR     : {iqr}")

    # Potential outlier boundaries using the IQR rule.
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    outlier_count = (
        (df_cleaned[col] < lower_bound)
        | (df_cleaned[col] > upper_bound)
    ).sum()

    print(f"Lower bound : {lower_bound:.2f}")
    print(f"Upper bound : {upper_bound:.2f}")
    print(f"Potential outliers : {outlier_count}")


# ---------------------------------------------------------------------------
# 8. BIVARIATE EDA - NUMERICAL FEATURES VS CHARGES
# BIVARIATE EDA focuses on analyzing the relationship between two variables.
# For numerical features, scatterplots and correlation coefficients are useful.
# ---------------------------------------------------------------------------

print("\n" + "=" * 80)
print("8. BIVARIATE EDA - NUMERICAL FEATURES VS CHARGES")
print("=" * 80)

# Scatterplots help us visually inspect relationships with the target.
features_vs_charges = ["age", "bmi", "children"]

for col in features_vs_charges:
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df_cleaned, x=col, y="charges")
    plt.title(f"{col} vs Charges")
    plt.xlabel(col)
    plt.ylabel("Charges")
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------------------
# 9. BIVARIATE EDA - CATEGORICAL FEATURES VS CHARGES
# ---------------------------------------------------------------------------

print("\n" + "=" * 80)
print("9. BIVARIATE EDA - CATEGORICAL FEATURES VS CHARGES")
print("=" * 80)

for col in categorical_columns:
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df_cleaned, x=col, y="charges")
    plt.title(f"{col} vs Charges")
    plt.xlabel(col)
    plt.ylabel("Charges")
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------------------
# 10. CORRELATION ANALYSIS
# Correlation analysis helps us understand the relationships between variables.
# ---------------------------------------------------------------------------

print("\n" + "=" * 80)
print("10. CORRELATION ANALYSIS")
print("=" * 80)

correlation_columns = ["age", "bmi", "children", "charges"]
correlation_matrix = df_cleaned[correlation_columns].corr()

print("\n--- Pearson correlation matrix ---")
print(correlation_matrix)

plt.figure(figsize=(8, 6))
sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    vmin=-1,
    vmax=1,
)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

print("\n--- Pearson correlation with charges ---")

for col in ["age", "bmi", "children"]:
    r, p_value = pearsonr(df_cleaned[col], df_cleaned["charges"])
    print(
        f"{col:10s} -> Pearson r = {r:.4f}, "
        f"p-value = {p_value:.6f}"
    )


# ---------------------------------------------------------------------------
# 11. FEATURE ENGINEERING - BMI CATEGORY
# Feature engineering is the process of creating new features from existing ones.
# ---------------------------------------------------------------------------

print("\n" + "=" * 80)
print("11. FEATURE ENGINEERING - BMI CATEGORY")
print("=" * 80)

# Keep the original BMI as a continuous value.
# Create a separate categorical feature for exploration.
df_cleaned["bmi_category"] = pd.cut(
    df_cleaned["bmi"],
    bins=[-np.inf, 18.5, 25, 30, np.inf],
    labels=["Underweight", "Normal", "Overweight", "Obesity"],
    right=False,
)

print("\n--- BMI category counts ---")
print(df_cleaned["bmi_category"].value_counts().sort_index())

plt.figure(figsize=(8, 4))
sns.countplot(
    data=df_cleaned,
    x="bmi_category",
    order=["Underweight", "Normal", "Overweight", "Obesity"],
)
plt.title("BMI Category Distribution")
plt.xlabel("BMI Category")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(data=df_cleaned, x="bmi_category", y="charges")
plt.title("BMI Category vs Charges")
plt.xlabel("BMI Category")
plt.ylabel("Charges")
plt.tight_layout()
plt.show()


# ---------------------------------------------------------------------------
# 12. STATISTICAL ANALYSIS - CHI-SQUARE
# Chi-square test is a statistical test used to determine if there is a significant association between two categorical variables.
# In this case, we will check the association between categorical features and the target variable 'charges' by dividing 'charges' into quartiles.
# ---------------------------------------------------------------------------

print("\n" + "=" * 80)
print("12. STATISTICAL ANALYSIS - CHI-SQUARE")
print("=" * 80)

"""
Chi-square requires categorical variables.

'charges' is continuous, so for this EDA learning exercise we divide it
into four quartile groups:

Q1, Q2, Q3, Q4

This means the Chi-square test checks association with CHARGE QUARTILE,
not the original continuous charges value.
"""

df_cleaned["charges_bin"] = pd.qcut(
    df_cleaned["charges"],
    q=4,
    labels=["Q1", "Q2", "Q3", "Q4"],
)

chi_square_features = ["sex", "smoker", "region", "bmi_category"]
alpha = 0.05

chi2_results = []

for col in chi_square_features:
    contingency_table = pd.crosstab(
        df_cleaned[col],
        df_cleaned["charges_bin"],
    )

    chi2_stat, p_value, degrees_of_freedom, expected = chi2_contingency(
        contingency_table
    )

    decision = (
        "Reject H0"
        if p_value < alpha
        else "Fail to Reject H0"
    )

    chi2_results.append(
        {
            "Feature": col,
            "Chi2 Statistic": chi2_stat,
            "p-value": p_value,
            "Degrees of Freedom": degrees_of_freedom,
            "Decision": decision,
        }
    )

    print(f"\n--- {col} ---")
    print("Contingency table:")
    print(contingency_table)
    print(f"Chi2 statistic : {chi2_stat:.4f}")
    print(f"p-value        : {p_value:.6f}")
    print(f"Decision       : {decision}")

chi2_df = pd.DataFrame(chi2_results)

print("\n--- Chi-square summary ---")
print(chi2_df.sort_values("p-value"))


# ---------------------------------------------------------------------------
# 13. SAVE EDA DATASET
# ---------------------------------------------------------------------------

print("\n" + "=" * 80)
print("13. SAVE EDA DATASET")
print("=" * 80)

OUTPUT_FILE = "insurance_eda_cleaned.csv"

df_cleaned.to_csv(OUTPUT_FILE, index=False)

print(f"EDA dataset saved to: {OUTPUT_FILE}")
print(f"Final EDA dataset shape: {df_cleaned.shape}")


# ---------------------------------------------------------------------------
# 14. EDA LEARNING SUMMARY
# ---------------------------------------------------------------------------

print("\n" + "=" * 80)
print("14. EDA LEARNING SUMMARY")
print("=" * 80)

print(
    """
This project covered:

1. Load Dataset
2. Understand Data
3. Data Quality
   - Missing values
   - Duplicate values
4. Numerical and Categorical Features
5. Univariate EDA
   - Histograms
   - KDE
   - Boxplots
   - Countplots
6. Five-number summary
7. IQR and potential outliers
8. Bivariate EDA
   - Numerical features vs charges
   - Categorical features vs charges
9. Correlation
   - Correlation matrix
   - Pearson correlation
10. Feature Engineering
    - BMI categories
11. Statistical Analysis
    - Chi-square test using charge quartiles

Next learning stage:
    Model Training → Model Evaluation

This file intentionally does NOT implement those stages yet.
"""
)

print("=" * 80)