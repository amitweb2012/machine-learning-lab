"""Covariance and Pearson correlation."""
import numpy as np

study_hours = np.array([1, 2, 3, 4, 5], dtype=float)
scores = np.array([52, 58, 65, 72, 80], dtype=float)

cov_matrix = np.cov(study_hours, scores, ddof=1)
correlation_matrix = np.corrcoef(study_hours, scores)

print("Covariance matrix:\n", cov_matrix)
print("Covariance:", cov_matrix[0, 1])
print("Pearson correlation:", correlation_matrix[0, 1])
