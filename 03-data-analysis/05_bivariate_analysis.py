"""Bivariate analysis: scatter plots and group comparisons."""
import matplotlib.pyplot as plt
import pandas as pd
from eda_utils import load_customer_data, save_figure

df = load_customer_data()

fig, ax = plt.subplots(figsize=(7, 5))
for churn_value, group in df.groupby("churn"):
    ax.scatter(group["satisfaction_score"], group["monthly_spend"], alpha=0.6, label=churn_value)
ax.set_title("Satisfaction vs monthly spend")
ax.set_xlabel("Satisfaction score")
ax.set_ylabel("Monthly spend")
ax.legend(title="Churn")
save_figure(fig, "scatter_satisfaction_vs_spend.png")
plt.close(fig)

summary = df.groupby("plan", observed=True)[["annual_income", "monthly_spend", "satisfaction_score"]].mean().round(2)
print("Mean numerical values by plan:\n", summary)

fig, ax = plt.subplots(figsize=(7, 4))
df.boxplot(column="monthly_spend", by="plan", ax=ax)
ax.set_title("Monthly spend by plan")
fig.suptitle("")
ax.set_xlabel("Plan")
ax.set_ylabel("Monthly spend")
save_figure(fig, "box_spend_by_plan.png")
plt.close(fig)
