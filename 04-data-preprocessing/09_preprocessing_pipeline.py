"""End-to-end preprocessing pipeline using insurance-style features."""
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


df = pd.DataFrame({
    "age": [25, 34, None, 45, 52, 41],
    "bmi": [22.1, 28.4, 31.2, None, 26.8, 29.5],
    "children": [0, 2, 1, 3, 0, 2],
    "smoker": ["no", "yes", "no", "no", "yes", "no"],
    "region": ["southwest", "southeast", "northwest", "northeast", "southwest", "northwest"],
})

numeric_features = ["age", "bmi", "children"]
categorical_features = ["smoker", "region"]

numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
])

preprocessor = ColumnTransformer([
    ("numeric", numeric_pipeline, numeric_features),
    ("categorical", categorical_pipeline, categorical_features),
])

X_transformed = preprocessor.fit_transform(df)
print("Original shape:", df.shape)
print("Transformed shape:", X_transformed.shape)
print("\nTransformed data:\n", X_transformed)
