"""Univariate analysis: histograms and box plots for numerical features."""
import matplotlib.pyplot as plt
from eda_utils import load_customer_data, save_figure

df = load_customer_data()
features = ["age", "annual_income", "monthly_spend", "tenure_months", "support_tickets", "satisfaction_score"]

for col in features:
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.hist(df[col], bins=20, edgecolor="black")
    ax.set_title(f"Distribution of {col}")
    ax.set_xlabel(col)
    ax.set_ylabel("Frequency")
    save_figure(fig, f"hist_{col}.png")
    plt.close(fig)

for col in features:
    fig, ax = plt.subplots(figsize=(7, 3.5))
    ax.boxplot(df[col], vert=False)
    ax.set_title(f"Box plot of {col}")
    ax.set_xlabel(col)
    save_figure(fig, f"box_{col}.png")
    plt.close(fig)
