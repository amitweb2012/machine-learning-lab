"""Five-number summary: min, Q1, median, Q3 and max."""
import numpy as np

values = np.array([4, 7, 8, 10, 12, 13, 15, 18, 21, 25, 30], dtype=float)
q1, median, q3 = np.percentile(values, [25, 50, 75])

print("Minimum:", values.min())
print("Q1:", q1)
print("Median:", median)
print("Q3:", q3)
print("Maximum:", values.max())
print("IQR:", q3 - q1)
