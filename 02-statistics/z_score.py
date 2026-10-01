"""Z-score: number of standard deviations an observation is from the mean."""
import numpy as np

scores = np.array([55, 60, 65, 70, 75, 80, 85], dtype=float)
x = 80
mu = scores.mean()
sigma = scores.std()
z = (x - mu) / sigma

print("Mean:", mu)
print("Population std:", sigma)
print("x:", x)
print("Z-score:", z)
