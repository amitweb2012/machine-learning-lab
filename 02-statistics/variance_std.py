"""Variance and standard deviation from first principles and NumPy."""
import numpy as np

x = np.array([10, 12, 14, 16, 18], dtype=float)
mean = x.mean()

population_variance = ((x - mean) ** 2).mean()
population_std = np.sqrt(population_variance)

sample_variance = ((x - mean) ** 2).sum() / (len(x) - 1)
sample_std = np.sqrt(sample_variance)

print("Mean:", mean)
print("Population variance:", population_variance)
print("Population std:", population_std)
print("Sample variance:", sample_variance)
print("Sample std:", sample_std)
