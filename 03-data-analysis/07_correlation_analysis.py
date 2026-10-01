"""Covariance/correlation analysis and a correlation heatmap."""
import matplotlib.pyplot as plt
import seaborn as sns
from eda_utils import load_customer_data, save_figure

df = load_customer_data()
numeric = df.select_dtypes("number")
print("Pearson correlation matrix:\n", numeric.corr().round(3))
print("\nCovariance matrix:\n", numeric.cov().round(2))

fig, ax = plt.subplots(figsize=(9, 7))
sns.heatmap(numeric.corr(), annot=True, fmt=".2f", cmap="coolwarm", center=0, ax=ax)
ax.set_title("Pearson Correlation Heatmap")
save_figure(fig, "correlation_heatmap.png")
plt.close(fig)
