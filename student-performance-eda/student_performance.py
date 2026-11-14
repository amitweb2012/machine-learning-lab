import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
warnings.filterwarnings("ignore")

path = Path(__file__).parent / "data" / "student_performance.csv"
df = pd.read_csv(path)
numeric_cols = df.select_dtypes(include=[np.number]).columns
numeric_features = [col for col in numeric_cols if col != "student_id"]
print("--- First 5 rows of the dataset ---")
print(df.head())
print("\n--- Summary Statistics ---")
print(df[numeric_features].describe())
print("\n--- Data Types ---")
print(df.dtypes)
print("\n--- Missing Values ---")
print(df.isnull().sum())
# Missing percentage
missing_percentage = (
    df.isnull().mean() * 100
)
print("\n--- Missing Values Percentage ---")
print(missing_percentage)
# fill missing values with mean for numeric columns
for col in numeric_features:
    df[col] = df[col].fillna(df[col].mean())

print("\n--- Duplicate Values ---")
print(df.duplicated().sum())
# remove duplicates and rows with missing values
df_cleaned = df.drop_duplicates().dropna()
print("\n--- Unique Values ---")
for col in df_cleaned.columns:
    print(f"{col}: {df_cleaned[col].nunique()}")
    
value_ranges = {
    "study_hours": (0, 24),
    "attendance": (0, 100),
    "math": (0, 100),
    "science": (0, 100),
    "english": (0, 100),
}

for col, (minimum, maximum) in value_ranges.items():
    invalid_values = df_cleaned[
        (df_cleaned[col] < minimum) | (df_cleaned[col] > maximum)
    ]
    if not invalid_values.empty:
        print(f"\n--- Invalid values in {col} ---")
        print(invalid_values)

mark_columns = {"math", "science", "english"}

for col, (minimum, maximum) in value_ranges.items():
    invalid_mask = (df_cleaned[col] < minimum) | (df_cleaned[col] > maximum)
    if invalid_mask.any():
        valid_values = df_cleaned.loc[~invalid_mask, col]
        if valid_values.empty:
            raise ValueError(f"No valid values available to clean {col}.")
        replacement_value = valid_values.mean()
        if col in mark_columns:
            replacement_value = int(np.floor(replacement_value + 0.5))
        else:
            df_cleaned[col] = df_cleaned[col].astype(float)
        df_cleaned.loc[invalid_mask, col] = replacement_value

print("\n--- First 5 rows of the cleaned dataset ---")
print(df_cleaned.head(20))


# Five number summary for numeric columns
numeric_features = [
    col
    for col in df_cleaned.select_dtypes(include=[np.number]).columns
    if col != "student_id"
]
for col in numeric_features:
    print(f"\n--- Five Number Summary for {col} ---")
    print("Minimum:", df_cleaned[col].min())
    print("First Quartile (Q1):", df_cleaned[col].quantile(0.25))
    print("Median (Q2):", df_cleaned[col].median())
    print("Third Quartile (Q3):", df_cleaned[col].quantile(0.75))
    print("Maximum:", df_cleaned[col].max())
    IQR = df_cleaned[col].quantile(0.75) - df_cleaned[col].quantile(0.25)
    lower_bound = df_cleaned[col].quantile(0.25) - 1.5 * IQR
    upper_bound = df_cleaned[col].quantile(0.75) + 1.5 * IQR
    print("Lower Bound:", lower_bound)
    print("Upper Bound:", upper_bound)
    # total number of outliers
    outliers = df_cleaned[(df_cleaned[col] < lower_bound) | (df_cleaned[col] > upper_bound)]
    print("Total Outliers:", outliers.shape[0])
    
features = ["study_hours", "attendance", "math", "science", "english"]
df_cleaned[features].hist(figsize=(12, 8), bins=10)
plt.tight_layout()
plt.show()

df_cleaned[features].plot(
    kind="box", subplots=True, layout=(2, 3), figsize=(12, 8)
)
plt.tight_layout()
plt.show()

sns.countplot(data=df_cleaned, x="gender")
plt.show()

# Bivariate analysis: study habits and gender versus average marks
mark_columns = ["math", "science", "english"]
df_cleaned["average_marks"] = df_cleaned[mark_columns].mean(axis=1)
# Bands: <70 Needs Improvement, 70-<80 Average, 80-<90 Good, and 90+ Excellent.
df_cleaned["performance"] = pd.cut(
    df_cleaned["average_marks"],
    bins=[-np.inf, 70, 80, 90, np.inf],
    labels=["Needs Improvement", "Average", "Good", "Excellent"],
    right=False,
)

print("\n--- Performance Category Counts ---")
print(df_cleaned["performance"].value_counts(sort=False))

relationship_columns = ["study_hours", "attendance", "average_marks"]
print("\n--- Correlation with average marks ---")
print(df_cleaned[relationship_columns].corr().round(2))

fig, axes = plt.subplots(1, 3, figsize=(16, 5))
sns.scatterplot(
    data=df_cleaned,
    x="study_hours",
    y="average_marks",
    hue="gender",
    ax=axes[0],
)
axes[0].set_title("Study Hours vs Average Marks")

sns.scatterplot(
    data=df_cleaned,
    x="attendance",
    y="average_marks",
    hue="gender",
    ax=axes[1],
)
axes[1].set_title("Attendance vs Average Marks")

sns.boxplot(data=df_cleaned, x="gender", y="average_marks", ax=axes[2])
axes[2].set_title("Average Marks by Gender")

plt.tight_layout()
plt.show()

# Multivariate analysis: correlations among measured features
correlation_features = ["study_hours", "attendance", *mark_columns]
correlation_matrix = df_cleaned[correlation_features].corr()

print("\n--- Multivariate Correlation Matrix ---")
print(correlation_matrix.round(2))

plt.figure(figsize=(8, 6))
sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    square=True,
)
plt.title("Correlations Between Study Habits and Subject Marks")
plt.tight_layout()
plt.show()

print("\n--- EDA Findings (Descriptive Only) ---")
print(f"Students analyzed: {len(df_cleaned)}")
print(f"Overall average marks: {df_cleaned['average_marks'].mean():.1f}")

top_student = df_cleaned.loc[df_cleaned["average_marks"].idxmax()]
bottom_student = df_cleaned.loc[df_cleaned["average_marks"].idxmin()]
print(
    f"Highest average: {top_student['name']} "
    f"({top_student['average_marks']:.1f})"
)
print(
    f"Lowest average: {bottom_student['name']} "
    f"({bottom_student['average_marks']:.1f})"
)

print("\nAverage marks by gender:")
print(df_cleaned.groupby("gender")["average_marks"].mean().round(1))

for feature in ["study_hours", "attendance"]:
    correlation = df_cleaned[feature].corr(df_cleaned["average_marks"])
    print(f"Correlation of {feature} with average marks: {correlation:.2f}")

print("These results are descriptive and do not establish causation.")

output_file = (
    Path(__file__).resolve().parent
    / "data"
    / "processed"
    / "student_performance_eda_cleaned.csv"
)
output_file.parent.mkdir(parents=True, exist_ok=True)
df_cleaned.to_csv(output_file, index=False)
print(f"\nCleaned EDA dataset saved to: {output_file}")

