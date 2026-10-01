"""Simple insurance-oriented feature engineering examples."""
import pandas as pd


df = pd.DataFrame({
    "age": [25, 40, 55],
    "bmi": [22.5, 28.0, 34.2],
    "children": [0, 2, 3],
    "smoker": [0, 1, 0],
})

# Domain-inspired interaction and nonlinear features.
df["age_squared"] = df["age"] ** 2
df["bmi_squared"] = df["bmi"] ** 2
df["age_bmi_interaction"] = df["age"] * df["bmi"]
df["has_children"] = (df["children"] > 0).astype(int)

print(df)
