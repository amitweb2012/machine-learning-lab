# 📐 Mathematical Explanation — Data Preprocessing

## Missing values

Median imputation replaces a missing observation with the sample median:

**x_missing ← median(X_observed)**

When building a model, the imputation statistic should be learned from training data only.

## Outliers and IQR

**IQR = Q3 − Q1**

**Lower fence = Q1 − 1.5 × IQR**

**Upper fence = Q3 + 1.5 × IQR**

Values outside the fences are potential outliers, not automatically errors.

## One-hot encoding

For `smoker = {yes, no}`:

```text
smoker_yes  smoker_no
1           0
0           1
```

For `k` categories, one-hot encoding can create `k` indicator columns. Some models use `k−1` with a reference category.

## Standardization

**z = (x − μ) / σ**

This expresses a feature in standard-deviation units and is useful for many scale-sensitive algorithms.

## Min-max scaling

**x' = (x − x_min) / (x_max − x_min)**

For non-constant training data, the training range is mapped approximately to `[0, 1]`.

## L2 normalization

For a vector `x`:

**x' = x / ||x||₂**

where **||x||₂ = √(x₁² + x₂² + ... + xₙ²)**.

Standardization operates feature-by-feature; normalization can operate row-by-row.

## Train/test split

For test proportion `p`:

**n_test ≈ p × n**

**n_train ≈ (1 − p) × n**

The test set should remain held out for final evaluation.

## Feature engineering

Examples:

**age_squared = age²**

**bmi_squared = bmi²**

**age_bmi_interaction = age × bmi**

These transformations can help models represent nonlinear effects or interactions.

## Preprocessing pipeline

A reproducible workflow is:

```text
Training data
    ↓
fit preprocessing
    ↓
transform training data
    ↓
fit model

Test/new data
    ↓
transform using fitted preprocessing
    ↓
predict
```

The preprocessing parameters must not be learned from the held-out test set; otherwise information can leak into training.
