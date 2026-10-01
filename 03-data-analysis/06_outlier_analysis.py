"""Detect potential outliers using the IQR rule."""
from eda_utils import load_customer_data

df = load_customer_data()
features = df.select_dtypes("number").columns

for col in features:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    mask = (df[col] < lower) | (df[col] > upper)
    print(f"{col}: Q1={q1:.2f}, Q3={q3:.2f}, IQR={iqr:.2f}, potential outliers={mask.sum()}")
