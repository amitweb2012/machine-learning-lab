"""Categorical analysis with bar charts and target proportions."""
import matplotlib.pyplot as plt
from eda_utils import load_customer_data, save_figure

df = load_customer_data()
for col in ["plan", "region", "churn"]:
    counts = df[col].value_counts()
    fig, ax = plt.subplots(figsize=(7, 4))
    counts.plot(kind="bar", ax=ax)
    ax.set_title(f"Count by {col}")
    ax.set_xlabel(col)
    ax.set_ylabel("Count")
    ax.tick_params(axis="x", rotation=0)
    save_figure(fig, f"bar_{col}.png")
    plt.close(fig)

print("Churn proportion:\n", df["churn"].value_counts(normalize=True).mul(100).round(2))
print("\nChurn by plan (%):\n", pd_crosstab := __import__("pandas").crosstab(df["plan"], df["churn"], normalize="index").mul(100).round(2))
