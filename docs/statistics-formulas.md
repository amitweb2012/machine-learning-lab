# Statistics Formula Sheet

## Mean

x̄ = (x₁ + x₂ + ... + xₙ) / n

## Variance

Population variance:

σ² = Σ(xᵢ − μ)² / N

Sample variance:

s² = Σ(xᵢ − x̄)² / (n − 1)

## Standard Deviation

σ = √σ²

## Z-score

z = (x − μ) / σ

## Covariance

Cov(X,Y) = Σ[(xᵢ − x̄)(yᵢ − ȳ)] / (n − 1)

## Correlation

r = Cov(X,Y) / (σₓ σᵧ)

## Confidence Interval for a Mean

x̄ ± critical_value × standard_error

## Five-Number Summary

- Minimum
- Q1
- Median
- Q3
- Maximum

## Common ML Metrics

MAE = (1/n) Σ|yᵢ − ŷᵢ|

MSE = (1/n) Σ(yᵢ − ŷᵢ)²

RMSE = √MSE

R² = 1 − SS_res / SS_tot

Accuracy = Correct / Total

Precision = TP / (TP + FP)

Recall = TP / (TP + FN)

F1 = 2 × Precision × Recall / (Precision + Recall)
