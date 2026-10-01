"""Confidence interval for a population mean using the t distribution."""
import numpy as np
from scipy import stats

sample = np.array([52, 55, 49, 61, 58, 54, 57, 53, 60, 56], dtype=float)
mean = sample.mean()
sem = stats.sem(sample)
confidence = 0.95
ci_low, ci_high = stats.t.interval(
    confidence, df=len(sample) - 1, loc=mean, scale=sem
)

print("Sample mean:", mean)
print("95% confidence interval:", (ci_low, ci_high))
