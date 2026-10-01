"""Use skewness and histograms to inspect distribution shape."""
import matplotlib.pyplot as plt
from scipy.stats import skew
from eda_utils import load_customer_data, save_figure

df = load_customer_data()
for col in df.select_dtypes("number").columns:
    value = skew(df[col], bias=False)
    print(f"{col}: skewness={value:.3f}")
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.hist(df[col], bins=20, density=True, alpha=0.75, edgecolor="black")
    ax.axvline(df[col].mean(), linestyle="--", label="Mean")
    ax.axvline(df[col].median(), linestyle=":", label="Median")
    ax.set_title(f"Distribution: {col}")
    ax.set_xlabel(col)
    ax.set_ylabel("Density")
    ax.legend()
    save_figure(fig, f"distribution_{col}.png")
    plt.close(fig)
