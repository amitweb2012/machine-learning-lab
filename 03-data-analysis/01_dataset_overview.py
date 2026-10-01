"""Inspect shape, columns, dtypes and descriptive statistics."""
from eda_utils import load_customer_data

df = load_customer_data()
print("Shape:", df.shape)
print("\nColumns:\n", df.columns.tolist())
print("\nData types:\n", df.dtypes)
print("\nFirst 5 rows:\n", df.head())
print("\nDescriptive statistics:\n", df.describe(include="all"))
