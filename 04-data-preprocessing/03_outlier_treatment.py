"""IQR-based potential outlier detection and winsorization example."""
import numpy as np
import pandas as pd


df = pd.DataFrame({"bmi": [21.2, 23.5, 24.1, 25.8, 26.4, 27.0, 28.2, 29.1, 45.0]})

q1 = df["bmi"].quantile(0.25)
q3 = df["bmi"].quantile(0.75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

mask = (df["bmi"] < lower) | (df["bmi"] > upper)
print("Q1:", q1, "Q3:", q3, "IQR:", iqr)
print("Lower fence:", lower, "Upper fence:", upper)
print("Potential outliers:\n", df[mask])

# Example treatment: clipping to IQR fences.
df["bmi_clipped"] = np.clip(df["bmi"], lower, upper)
print("\nAfter clipping:\n", df)
