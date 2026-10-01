"""Examples of common probability distributions."""
import numpy as np
from scipy.stats import binom, norm, poisson

# Binomial: exactly 3 successes in 10 trials with p=0.5
print("Binomial P(X=3):", binom.pmf(3, n=10, p=0.5))

# Normal: probability below x=1.96 for standard normal
print("Normal P(X<=1.96):", norm.cdf(1.96))

# Poisson: exactly 4 events when lambda=3
print("Poisson P(X=4):", poisson.pmf(4, mu=3))

# Generate a small normal sample and summarize it.
sample = np.random.default_rng(42).normal(loc=100, scale=15, size=1000)
print("Sample mean:", sample.mean())
print("Sample std:", sample.std())
