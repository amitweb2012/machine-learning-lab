"""
Student Exam Performance - Exploratory Data Analysis (EDA)

EDA Pipeline
------------
1. Load Dataset
2. Understand Data
3. Data Quality
4. Numerical & Categorical Features
5. Univariate EDA - Numerical
6. Univariate EDA - Categorical
7. Five-Number Summary & IQR
8. Bivariate EDA - Numerical vs Numerical
9. Bivariate EDA - Categorical vs Numerical
10. Bivariate EDA - Categorical vs Categorical
11. Correlation Analysis
12. Statistical Analysis

This project intentionally stops at EDA/statistical analysis.
Model training and model evaluation are NOT included.
"""

import warnings

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import chi2_contingency, pearsonr

warnings.filterwarnings("ignore")

sns.set_theme(style="whitegrid")


# ============================================================================
# 1. LOAD DATASET
# ============================================================================

DATA_FILE = "student_exam_performance.csv"

print("\n" + "=" * 80)
print("1. LOAD DATASET")
print("=" * 80)

df = pd.read_csv(DATA_FILE)

print(f"Dataset: {DATA_FILE}")
print(f"Shape: {df.shape}")


# ============================================================================
# 2. UNDERSTAND DATA
# ============================================================================

print("\n" + "=" * 80)
print("2. UNDERSTAND DATA")
print("=" * 80)

print("\n--- First 5 rows ---")
print(df.head())

print("\n--- Last 5 rows ---")
print(df.tail())

print("\n--- Shape ---")
print(df.shape)

print("\n--- Dataset Information ---")
df.info()

print("\n--- Descriptive Statistics ---")
print(df.describe())

print("\n--- Column Names ---")
print(df.columns.tolist())

print("\n--- Data Types ---")
print(df.dtypes)


# ============================================================================
# 3. DATA QUALITY
# ============================================================================

print("\n" + "=" * 80)
print("3. DATA QUALITY")
print("=" * 80)


# ---------------------------------------------------------------------------
# 3.1 Missing Values
# ---------------------------------------------------------------------------

print("\n--- Missing Values ---")

missing_values = df.isnull().sum()

print(missing_values[missing_values > 0])


print("\n--- Missing Value Percentage ---")

missing_percentage = (
    df.isnull().mean() * 100
).round(2)

print(missing_percentage[missing_percentage > 0])


# ---------------------------------------------------------------------------
# 3.2 Duplicate Rows
# ---------------------------------------------------------------------------

print("\n--- Duplicate Rows ---")

duplicate_count = df.duplicated().sum()

print(f"Duplicate rows: {duplicate_count}")


# ---------------------------------------------------------------------------
# 3.3 Clean Dataset
# ---------------------------------------------------------------------------

df_cleaned = df.copy()

df_cleaned.drop_duplicates(inplace=True)
df_cleaned.dropna(inplace=True)

print("\n--- Shape After Cleaning ---")
print(df_cleaned.shape)

print("\n--- Missing Values After Cleaning ---")
print(df_cleaned.isnull().sum().sum())

print("\n--- Duplicate Rows After Cleaning ---")
print(df_cleaned.duplicated().sum())


# ============================================================================
# 4. NUMERICAL AND CATEGORICAL FEATURES
# ============================================================================

print("\n" + "=" * 80)
print("4. NUMERICAL AND CATEGORICAL FEATURES")
print("=" * 80)


# ---------------------------------------------------------------------------
# ID Columns
# ---------------------------------------------------------------------------

id_columns = [
    "student_id"
]


# ---------------------------------------------------------------------------
# Numerical Columns
# ---------------------------------------------------------------------------

numeric_columns = [
    "age",
    "previous_exam_score",
    "previous_gpa",
    "attendance_percentage",
    "assignment_completion_rate",
    "study_hours_per_day",
    "self_study_hours",
    "private_tuition",
    "online_learning_hours",
    "practice_tests_completed",
    "sleep_hours",
    "daily_screen_time",
    "physical_activity_hours",
    "stress_level",
    "internet_access",
    "online_course_hours",
    "exam_preparation_days",
    "questions_attempted",
    "questions_correct",
    "time_management_score",
    "exam_anxiety_level",
    "exam_score"
]


# ---------------------------------------------------------------------------
# Target / Outcome Columns
# ---------------------------------------------------------------------------

target_columns = [
    "performance_grade",
    "pass_status",
    "performance_level"
]


# ---------------------------------------------------------------------------
# Categorical Columns
# ---------------------------------------------------------------------------

categorical_columns = [
    col
    for col in df_cleaned.select_dtypes(
        include=["object", "category"]
    ).columns
    if col not in id_columns
]


# Remove target columns from categorical input features

categorical_features = [
    col
    for col in categorical_columns
    if col not in target_columns
]


print("\nID Columns:")
print(id_columns)

print("\nNumerical Columns:")
print(numeric_columns)

print("\nCategorical Features:")
print(categorical_features)

print("\nTarget Columns:")
print(target_columns)


# ============================================================================
# 5. UNIVARIATE EDA - NUMERICAL FEATURES
# ============================================================================

print("\n" + "=" * 80)
print("5. UNIVARIATE EDA - NUMERICAL FEATURES")
print("=" * 80)


for col in numeric_columns:

    print(f"\n--- {col} ---")

    print(df_cleaned[col].describe())

    # Histogram
    plt.figure(figsize=(8, 4))

    sns.histplot(
        data=df_cleaned,
        x=col,
        kde=True
    )

    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()

    # Boxplot
    plt.figure(figsize=(8, 3))

    sns.boxplot(
        data=df_cleaned,
        x=col
    )

    plt.title(f"Boxplot of {col}")
    plt.xlabel(col)

    plt.tight_layout()
    plt.show()


# ============================================================================
# 6. UNIVARIATE EDA - CATEGORICAL FEATURES
# ============================================================================

print("\n" + "=" * 80)
print("6. UNIVARIATE EDA - CATEGORICAL FEATURES")
print("=" * 80)


for col in categorical_features:

    print(f"\n--- {col} ---")

    print(
        df_cleaned[col]
        .value_counts()
    )

    plt.figure(figsize=(8, 4))

    order = (
        df_cleaned[col]
        .value_counts()
        .index
    )

    sns.countplot(
        data=df_cleaned,
        x=col,
        order=order
    )

    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Count")

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()
    plt.show()


# ============================================================================
# 6.1 TARGET / OUTCOME ANALYSIS
# ============================================================================

print("\n" + "=" * 80)
print("6.1 TARGET / OUTCOME ANALYSIS")
print("=" * 80)


for col in target_columns:

    print(f"\n--- {col} ---")

    print(
        df_cleaned[col]
        .value_counts()
    )

    plt.figure(figsize=(8, 4))

    order = (
        df_cleaned[col]
        .value_counts()
        .index
    )

    sns.countplot(
        data=df_cleaned,
        x=col,
        order=order
    )

    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Count")

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()
    plt.show()


# ============================================================================
# 7. FIVE-NUMBER SUMMARY AND IQR
# ============================================================================

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

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    outlier_count = (
        (df_cleaned[col] < lower_bound)
        |
        (df_cleaned[col] > upper_bound)
    ).sum()

    print(f"\n--- {col} ---")

    print(f"Minimum           : {minimum:.2f}")
    print(f"Q1                : {q1:.2f}")
    print(f"Median            : {median:.2f}")
    print(f"Q3                : {q3:.2f}")
    print(f"Maximum           : {maximum:.2f}")
    print(f"IQR               : {iqr:.2f}")
    print(f"Lower Bound       : {lower_bound:.2f}")
    print(f"Upper Bound       : {upper_bound:.2f}")
    print(f"Potential Outliers: {outlier_count}")


# ============================================================================
# 8. BIVARIATE EDA - NUMERICAL vs NUMERICAL
# ============================================================================

print("\n" + "=" * 80)
print("8. BIVARIATE EDA - NUMERICAL vs NUMERICAL")
print("=" * 80)


numerical_pairs = [

    ("previous_exam_score", "exam_score"),

    ("previous_gpa", "exam_score"),

    ("attendance_percentage", "exam_score"),

    ("assignment_completion_rate", "exam_score"),

    ("study_hours_per_day", "exam_score"),

    ("self_study_hours", "exam_score"),

    ("practice_tests_completed", "exam_score"),

    ("questions_correct", "exam_score"),

    ("exam_anxiety_level", "exam_score"),

    ("stress_level", "exam_score"),

]


for x_col, y_col in numerical_pairs:

    correlation = (
        df_cleaned[x_col]
        .corr(df_cleaned[y_col])
    )

    print(f"\n{x_col} vs {y_col}")
    print(f"Correlation: {correlation:.3f}")

    plt.figure(figsize=(8, 5))

    sns.scatterplot(
        data=df_cleaned,
        x=x_col,
        y=y_col,
        alpha=0.3
    )

    plt.title(
        f"{x_col} vs {y_col}\n"
        f"Correlation = {correlation:.3f}"
    )

    plt.xlabel(x_col)
    plt.ylabel(y_col)

    plt.tight_layout()
    plt.show()


# ============================================================================
# 9. BIVARIATE EDA - CATEGORICAL vs NUMERICAL
# ============================================================================

print("\n" + "=" * 80)
print("9. BIVARIATE EDA - CATEGORICAL vs NUMERICAL")
print("=" * 80)


categorical_numeric_pairs = [

    ("gender", "exam_score"),

    ("family_income", "exam_score"),

    ("study_consistency", "exam_score"),

    ("study_method", "exam_score"),

    ("sleep_quality", "exam_score"),

    ("motivation_level", "exam_score"),

    ("exam_difficulty", "exam_score"),

]


for cat_col, num_col in categorical_numeric_pairs:

    print(f"\n--- {cat_col} vs {num_col} ---")

    summary = (
        df_cleaned
        .groupby(cat_col)[num_col]
        .agg(
            count="count",
            mean="mean",
            median="median",
            std="std"
        )
        .round(2)
    )

    print(summary)

    plt.figure(figsize=(9, 5))

    sns.boxplot(
        data=df_cleaned,
        x=cat_col,
        y=num_col
    )

    plt.title(
        f"{cat_col} vs {num_col}"
    )

    plt.xlabel(cat_col)
    plt.ylabel(num_col)

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()
    plt.show()


# ============================================================================
# 10. BIVARIATE EDA - CATEGORICAL vs CATEGORICAL
# ============================================================================

print("\n" + "=" * 80)
print("10. BIVARIATE EDA - CATEGORICAL vs CATEGORICAL")
print("=" * 80)


categorical_pairs = [

    ("gender", "pass_status"),

    ("study_consistency", "pass_status"),

    ("motivation_level", "pass_status"),

    ("exam_difficulty", "performance_level"),

    ("family_income", "performance_level"),

]


for col1, col2 in categorical_pairs:

    print(f"\n--- {col1} vs {col2} ---")

    contingency_table = pd.crosstab(
        df_cleaned[col1],
        df_cleaned[col2]
    )

    print("\nContingency Table:")
    print(contingency_table)

    # Chi-square test
    chi2, p_value, dof, expected = chi2_contingency(
        contingency_table
    )

    print(f"\nChi-square : {chi2:.3f}")
    print(f"p-value    : {p_value:.6f}")
    print(f"Degrees of freedom: {dof}")

    if p_value < 0.05:
        print("Result: Statistically significant association")
    else:
        print("Result: No statistically significant association")

    # Stacked percentage chart

    percentage_table = pd.crosstab(
        df_cleaned[col1],
        df_cleaned[col2],
        normalize="index"
    ) * 100

    percentage_table.plot(
        kind="bar",
        stacked=True,
        figsize=(9, 5)
    )

    plt.title(
        f"{col1} vs {col2}"
    )

    plt.xlabel(col1)
    plt.ylabel("Percentage")

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.legend(
        title=col2,
        bbox_to_anchor=(1.05, 1),
        loc="upper left"
    )

    plt.tight_layout()
    plt.show()


# ============================================================================
# 11. CORRELATION ANALYSIS
# ============================================================================

print("\n" + "=" * 80)
print("11. CORRELATION ANALYSIS")
print("=" * 80)


# ---------------------------------------------------------------------------
# 11.1 Correlation Matrix
# ---------------------------------------------------------------------------

correlation_matrix = (
    df_cleaned[numeric_columns]
    .corr()
)


print("\n--- Correlation Matrix ---")

print(
    correlation_matrix
    .round(2)
)


# ---------------------------------------------------------------------------
# 11.2 Heatmap
# ---------------------------------------------------------------------------

plt.figure(
    figsize=(20, 16)
)

sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0,
    square=True
)

plt.title(
    "Correlation Matrix of Numerical Features"
)

plt.tight_layout()
plt.show()


# ---------------------------------------------------------------------------
# 11.3 Correlation with Exam Score
# ---------------------------------------------------------------------------

exam_score_correlation = (
    correlation_matrix["exam_score"]
    .sort_values(
        ascending=False
    )
)


print("\n--- Correlation with Exam Score ---")

print(
    exam_score_correlation
    .round(3)
)


# ---------------------------------------------------------------------------
# 11.4 Strongest Positive / Negative Correlations
# ---------------------------------------------------------------------------

correlation_without_target = (
    exam_score_correlation
    .drop("exam_score")
)


strongest_positive = (
    correlation_without_target
    .sort_values(
        ascending=False
    )
    .head(5)
)


strongest_negative = (
    correlation_without_target
    .sort_values(
        ascending=True
    )
    .head(5)
)


print("\n--- Strongest Positive Correlations with Exam Score ---")

print(
    strongest_positive
    .round(3)
)


print("\n--- Strongest Negative Correlations with Exam Score ---")

print(
    strongest_negative
    .round(3)
)


# ---------------------------------------------------------------------------
# 11.5 Bar Chart - Correlation with Exam Score
# ---------------------------------------------------------------------------

plt.figure(
    figsize=(10, 8)
)

exam_score_correlation.drop(
    "exam_score"
).sort_values().plot(
    kind="barh"
)

plt.title(
    "Correlation of Numerical Features with Exam Score"
)

plt.xlabel("Pearson Correlation")
plt.ylabel("Feature")

plt.tight_layout()
plt.show()


# ============================================================================
# 11.6 Pearson Correlation Test
# ============================================================================

print("\n--- Pearson Correlation Tests ---")


pearson_results = []


for col in numeric_columns:

    if col == "exam_score":
        continue

    correlation, p_value = pearsonr(
        df_cleaned[col],
        df_cleaned["exam_score"]
    )

    pearson_results.append(
        {
            "feature": col,
            "correlation": correlation,
            "p_value": p_value
        }
    )


pearson_df = (
    pd.DataFrame(pearson_results)
    .sort_values(
        by="correlation",
        ascending=False
    )
)


print(
    pearson_df
    .round(4)
)


# ============================================================================
# 12. FINAL EDA SUMMARY
# ============================================================================

print("\n" + "=" * 80)
print("12. FINAL EDA SUMMARY")
print("=" * 80)


print(f"""
Dataset
-------
Original rows       : {len(df)}
Cleaned rows        : {len(df_cleaned)}
Original columns    : {df.shape[1]}

Features
--------
Numerical features  : {len(numeric_columns)}
Categorical features: {len(categorical_features)}
Target columns      : {len(target_columns)}

Main target
-----------
exam_score

EDA Completed
-------------
✓ Dataset loading
✓ Dataset understanding
✓ Missing-value analysis
✓ Duplicate analysis
✓ Data cleaning
✓ Numerical feature analysis
✓ Categorical feature analysis
✓ Target analysis
✓ Five-number summary
✓ IQR and outlier detection
✓ Numerical vs numerical analysis
✓ Categorical vs numerical analysis
✓ Categorical vs categorical analysis
✓ Chi-square analysis
✓ Correlation matrix
✓ Exam-score correlation analysis
✓ Pearson correlation testing

Next Steps
----------
1. Feature engineering
2. Feature selection
3. Encoding categorical variables
4. Train/test split
5. Machine learning model
6. Model evaluation
""")

print("=" * 80)
print("EDA COMPLETED")
print("=" * 80)