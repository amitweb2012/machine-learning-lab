"""Train/test split with an insurance-style regression target."""
import pandas as pd
from sklearn.model_selection import train_test_split


df = pd.DataFrame({
    "age": [23, 31, 45, 52, 28, 39, 61, 47, 35, 50],
    "bmi": [22.1, 27.3, 31.2, 29.8, 24.5, 26.7, 33.0, 30.1, 25.2, 28.9],
    "smoker": [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    "charges": [1200, 5400, 4300, 5100, 2100, 7800, 6200, 6900, 3000, 4700],
})

X = df.drop(columns="charges")
y = df["charges"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training rows:", len(X_train))
print("Testing rows:", len(X_test))
print("\nTraining features:\n", X_train)
print("\nTesting features:\n", X_test)
