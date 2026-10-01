"""Missing-value handling with an insurance-style dataset."""
import pandas as pd


df = pd.DataFrame({
    "age": [25, 34, None, 45, 52],
    "bmi": [22.1, None, 28.4, 31.2, 26.8],
    "charges": [1200, 2400, 3100, None, 4200],
})

print("Missing values before:\n", df.isna().sum())

# Median imputation is often useful for numeric features when robustness
# to extreme values is desirable.
for column in df.select_dtypes(include="number"):
    df[column] = df[column].fillna(df[column].median())

print("\nAfter median imputation:\n", df)
print("\nMissing values after:\n", df.isna().sum())
