"""Categorical encoding examples using an insurance-style dataset."""
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


df = pd.DataFrame({
    "sex": ["female", "male", "female", "male"],
    "smoker": ["yes", "no", "no", "yes"],
    "region": ["southwest", "southeast", "northwest", "northeast"],
})

encoder = ColumnTransformer(
    [("categorical", OneHotEncoder(handle_unknown="ignore", sparse_output=False), df.columns)],
    remainder="drop",
)

encoded = encoder.fit_transform(df)
print("Encoded shape:", encoded.shape)
print(encoded)
