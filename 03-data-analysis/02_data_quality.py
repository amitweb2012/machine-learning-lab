"""Check missing values, duplicates, unique values and basic ranges."""
from eda_utils import load_customer_data

df = load_customer_data()
print("Missing values:\n", df.isna().sum())
print("\nDuplicate rows:", df.duplicated().sum())
print("\nUnique values:\n", df.nunique())
print("\nNumerical ranges:\n", df.select_dtypes("number").agg(["min", "max"]).T)
print("\nCategorical value counts:")
for col in df.select_dtypes(exclude="number"):
    print(f"\n{col}\n{df[col].value_counts()}")
