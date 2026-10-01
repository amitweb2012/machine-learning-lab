"""Run a compact end-to-end EDA report and create key visualizations."""
import matplotlib.pyplot as plt
import seaborn as sns
from eda_utils import load_customer_data, save_figure

df = load_customer_data()

print("=== DATASET OVERVIEW ===")
print("Shape:", df.shape)
print("\nDtypes:\n", df.dtypes)
print("\nMissing values:\n", df.isna().sum())
print("\nDuplicate rows:", df.duplicated().sum())

print("\n=== NUMERICAL SUMMARY ===")
print(df.describe().T.round(2))

print("\n=== CATEGORICAL SUMMARY ===")
for col in df.select_dtypes(exclude="number"):
    print(f"\n{col}:\n{df[col].value_counts()}")

print("\n=== CORRELATION WITH MONTHLY SPEND ===")
print(df.select_dtypes("number").corr()["monthly_spend"].sort_values(ascending=False).round(3))

fig, axes = plt.subplots(2, 2, figsize=(12, 9))
sns.histplot(df["monthly_spend"], kde=True, ax=axes[0, 0])
axes[0, 0].set_title("Monthly spend distribution")
sns.boxplot(x=df["monthly_spend"], ax=axes[0, 1])
axes[0, 1].set_title("Monthly spend box plot")
sns.scatterplot(data=df, x="satisfaction_score", y="monthly_spend", hue="churn", ax=axes[1, 0])
axes[1, 0].set_title("Satisfaction vs monthly spend")
corr = df.select_dtypes("number").corr()
sns.heatmap(corr, cmap="coolwarm", center=0, ax=axes[1, 1])
axes[1, 1].set_title("Correlation matrix")
save_figure(fig, "complete_eda_dashboard.png")
plt.close(fig)
