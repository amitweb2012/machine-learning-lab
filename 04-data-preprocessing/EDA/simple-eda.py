from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

data = {
    "Student": [
        "Rahul", "Priya", "Amit", "Sneha",
        "Ravi", "Neha", "Arjun", "Pooja"
    ],
    "Age": [12, 13, 12, 13, 12, 13, 12, 13],
    "Gender": [
        "Male", "Female", "Male", "Female",
        "Male", "Female", "Male", "Female"
    ],
    "Math": [85, 92, 70, 95, 60, 88, 75, 90],
    "Science": [90, 88, 75, 92, 65, 85, 80, 94],
    "English": [78, 95, 80, 90, 70, 92, 72, 88]
}

df = pd.DataFrame(data)

print(df)

print("\n--- Summary Statistics ---")
print(df.describe())
print("\n--- Data Types ---")
print(df.dtypes)
print("\n--- Missing Values ---")
print(df.isnull().sum())
print("\n--- Duplicate Values ---")
print(df.duplicated().sum())
print("\n--- Unique Values ---")
for col in df.columns:
    print(f"{col}: {df[col].nunique()}")

# Univariate Analysis
numeric_cols = df.select_dtypes(include=[np.number]).columns
# for col in numeric_cols:
#     print(f"Mean of {col}:", df[col].mean())
#     print(f"Median of {col}:", df[col].median())
#     print(f"Mode of {col}:", df[col].mode()[0])
#     print(f"Minimum of {col}:", df[col].min())
#     print(f"Maximum of {col}:", df[col].max())
#     print(f"Standard Deviation of {col}:", df[col].std())
#     plt.figure(figsize=(8, 4))
#     sns.histplot(df[col], kde=True, bins=5)
#     plt.title(f"Distribution of {col}")
#     plt.xlabel(col)
#     plt.ylabel("Number of Students")
#     plt.show()

# Bivariate Analysis between marks

bivariate_cols = ["Math", "Science", "English"]
for i in range(len(bivariate_cols)):
    for j in range(i + 1, len(bivariate_cols)):
        col1 = bivariate_cols[i]
        col2 = bivariate_cols[j]
        # plt.figure(figsize=(8, 4))
        # sns.scatterplot(x=df[col1], y=df[col2], hue=df["Gender"])
        # plt.title(f"{col1} vs {col2}")
        # plt.xlabel(col1)
        # plt.ylabel(col2)
        # plt.tight_layout()
        # plt.show()

# Multivariate analysis

sns.heatmap(
    df[["Math", "Science", "English"]].corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Subject Correlation")
plt.show()

# Five number summary for each subject
for col in bivariate_cols:
    print(f"\n--- Five Number Summary for {col} ---")
    print("Minimum:", df[col].min())
    print("First Quartile (Q1):", df[col].quantile(0.25))
    print("Median (Q2):", df[col].median())
    print("Third Quartile (Q3):", df[col].quantile(0.75))
    print("Maximum:", df[col].max())
    lower_bound = df[col].quantile(0.25) - 1.5 * (df[col].quantile(0.75) - df[col].quantile(0.25))
    upper_bound = df[col].quantile(0.75) + 1.5 * (df[col].quantile(0.75) - df[col].quantile(0.25))
    print("Lower Bound for Outliers:", lower_bound)
    print("Upper Bound for Outliers:", upper_bound)
    IQR = df[col].quantile(0.75) - df[col].quantile(0.25)
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    print("Outliers:\n", outliers)
    
# show boxplots for each subject with outliers
for col in bivariate_cols:
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.xlabel(col)
    plt.tight_layout()
    plt.show()
    
# clean the dataset by removing outliers
df_cleaned = df.copy()
for col in bivariate_cols:
    lower_bound = df_cleaned[col].quantile(0.25) - 1.5 * (df_cleaned[col].quantile(0.75) - df_cleaned[col].quantile(0.25))
    upper_bound = df_cleaned[col].quantile(0.75) + 1.5 * (df_cleaned[col].quantile(0.75) - df_cleaned[col].quantile(0.25))
    df_cleaned = df_cleaned[(df_cleaned[col] >= lower_bound) & (df_cleaned[col] <= upper_bound)]

print("\n--- Cleaned Dataset ---")
print(df_cleaned)

# Feature Engineering: Create a new feature "Total Marks" by summing up the marks of all subjects
df_cleaned["Total Marks"] = df_cleaned["Math"] + df_cleaned["Science"] + df_cleaned["English"]
df_cleaned["Average Marks"] = df_cleaned["Total Marks"] / 3

def performance(avg):
    if avg >= 90:
        return "Excellent"
    elif avg >= 80:
        return "Good"
    elif avg >= 70:
        return "Average"
    else:
        return "Needs Improvement"

df_cleaned["Performance"] = df_cleaned["Average Marks"].apply(performance)

print("\n--- Dataset with New Features ---")
print(df_cleaned)

print("\n" + "=" * 80)
print("13. SAVE EDA DATASET")
print("=" * 80)

OUTPUT_FILE = Path(__file__).resolve().parent / "student_simple_eda_cleaned.csv"

df_cleaned.to_csv(OUTPUT_FILE, index=False)

print(f"EDA dataset saved to: {OUTPUT_FILE}")
print(f"Final EDA dataset shape: {df_cleaned.shape}")