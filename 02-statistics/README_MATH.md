# Statistics — Mathematical Guide

This guide explains the formulas used by the Python examples in this folder.

## 1. Descriptive Statistics

Mean: `x̄ = Σxᵢ / n`

Median: middle value after sorting. Mode: most frequent value. Range: `max − min`.

## 2. Probability

For equally likely outcomes: `P(A) = favorable / total`.

`0 ≤ P(A) ≤ 1` and `P(Aᶜ) = 1 − P(A)`.

## 3. Conditional Probability

`P(A | B) = P(A ∩ B) / P(B)` for `P(B) > 0`.

## 4. Bayes' Theorem

`P(A | B) = P(B | A)P(A) / P(B)`.

`P(A)` is the prior, `P(B|A)` the likelihood, and `P(A|B)` the posterior.

## 5. Distributions

Normal density: `f(x) = 1/(σ√(2π)) × exp(−(x−μ)²/(2σ²))`.

Binomial: `P(X=k) = C(n,k)pᵏ(1−p)ⁿ⁻ᵏ`.

Poisson: `P(X=k) = e⁻λ λᵏ / k!`.

## 6. Variance and Standard Deviation

Population variance: `σ² = Σ(xᵢ−μ)² / N`.

Sample variance: `s² = Σ(xᵢ−x̄)² / (n−1)`.

Standard deviation: `σ = √σ²`.

## 7. Covariance and Correlation

`Cov(X,Y) = Σ[(xᵢ−x̄)(yᵢ−ȳ)]/(n−1)`.

Pearson correlation: `r = Cov(X,Y)/(σₓσᵧ)`, with `−1 ≤ r ≤ 1`.

Correlation describes linear association and does not by itself establish causation.

## 8. Z-score

`z = (x−μ)/σ`.

It measures distance from the mean in standard-deviation units.

## 9. Hypothesis Testing

`H₀` is the null hypothesis; `H₁`/`Hₐ` is the alternative. A common significance level is `α=0.05`.

One-sample t statistic: `t = (x̄−μ₀)/(s/√n)`.

A p-value measures how extreme the observed result is under H₀ and the test assumptions. `p < α` is a common rule for rejecting H₀; failing to reject does not prove H₀ true.

## 10. Confidence Intervals

For an appropriate t-based mean interval: `x̄ ± t* × (s/√n)`.

A 95% interval refers to long-run procedure coverage under its assumptions.

## 11. Five-number Summary

Minimum, Q1, median, Q3, maximum.

`IQR = Q3 − Q1`.

A common box-plot rule flags potential outliers below `Q1−1.5×IQR` or above `Q3+1.5×IQR`.

## Machine Learning connection

`Statistics → EDA → Feature Engineering → Modeling → Evaluation → Experimentation`
