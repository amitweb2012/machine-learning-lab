"""Shared reproducible dataset and plotting helpers for the EDA examples."""
from pathlib import Path
import numpy as np
import pandas as pd

OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


def load_customer_data(seed=42, n=300):
    rng = np.random.default_rng(seed)
    age = rng.integers(18, 71, n)
    income = np.clip(rng.normal(65000, 22000, n), 18000, 160000)
    tenure = rng.integers(1, 73, n)
    plan = rng.choice(["Basic", "Standard", "Premium"], n, p=[0.40, 0.40, 0.20])
    region = rng.choice(["East", "West", "North", "South"], n)
    support = rng.poisson(2.2, n)
    satisfaction = np.clip(rng.normal(7.2, 1.5, n), 1, 10)
    monthly_spend = np.clip(35 + 0.00055 * income + 7 * (plan == "Standard") + 18 * (plan == "Premium") + rng.normal(0, 12, n), 20, 220)
    churn_score = 0.7 * (satisfaction < 6) + 0.45 * (support >= 4) + 0.35 * (tenure < 12) - 0.25 * (plan == "Premium") + rng.normal(0, 0.35, n)
    churn = np.where(churn_score > 0.55, "Yes", "No")
    return pd.DataFrame({
        "age": age, "annual_income": income.round(2), "monthly_spend": monthly_spend.round(2),
        "tenure_months": tenure, "support_tickets": support,
        "satisfaction_score": satisfaction.round(2), "plan": plan, "region": region, "churn": churn
    })


def save_figure(fig, name):
    path = OUTPUT_DIR / name
    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"Saved: {path}")
