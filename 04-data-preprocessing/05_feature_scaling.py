"""Standardization and min-max scaling."""
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler


df = pd.DataFrame({"age": [20, 30, 40, 50], "charges": [1000, 3000, 5000, 9000]})

standardized = StandardScaler().fit_transform(df)
minmax = MinMaxScaler().fit_transform(df)

print("Original:\n", df)
print("\nStandardScaler:\n", standardized)
print("\nMinMaxScaler:\n", minmax)
