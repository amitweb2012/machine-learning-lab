"""Detect and remove duplicate insurance-style records."""
import pandas as pd


df = pd.DataFrame({
    "age": [25, 34, 34, 45],
    "bmi": [22.1, 28.4, 28.4, 31.2],
    "charges": [1200, 2400, 2400, 3100],
})

print("Duplicate rows:", df.duplicated().sum())
print("\nDuplicate mask:\n", df.duplicated())

df_clean = df.drop_duplicates().reset_index(drop=True)
print("\nAfter removing duplicates:\n", df_clean)
