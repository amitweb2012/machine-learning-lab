"""Row-wise normalization using sklearn."""
import numpy as np
from sklearn.preprocessing import Normalizer

X = np.array([
    [25.0, 50000.0],
    [40.0, 80000.0],
    [60.0, 120000.0],
])

normalized = Normalizer(norm="l2").fit_transform(X)

print("Original:\n", X)
print("\nL2-normalized rows:\n", normalized)
print("\nRow norms:", np.linalg.norm(normalized, axis=1))
