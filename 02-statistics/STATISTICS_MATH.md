# Statistics Mathematical Explanation

This document explains the mathematics behind the Python examples in this folder.

## 1. Descriptive Statistics

Mean: `x̄ = Σxᵢ / n`

Median: middle value after sorting.

Mode: most frequent value.

Range: `max − min`.

Use descriptive statistics to summarize observed data before modeling.

## 2. Probability

For equally likely outcomes:

`P(A) = favorable outcomes / total outcomes`

Bounds: `0 ≤ P(A) ≤ 1`.

Complement: `P(Aᶜ) = 1 − P(A)`.

## 3. Conditional Probability

`P(A | B) = P(A ∩ B) / P(B)` for `P(B) > 0`.

It answers the probability of A after learning that B occurred.

## 4. Bayes' Theorem

`P(A | B) = P(B | A)P(A) / P(B)`.

Prior → likelihood + evidence → posterior.

Bayesian reasoning is useful in classification and probabilistic inference.

## 5. Distributions

### Normal

`f(x) = 1/(σ√(2π)) × exp(−(x−μ)²/(2σ²))`

### Binomial

`P(X=k) = C(n,k)pᵏ(1−p)ⁿ⁻ᵏ`

### Poisson

`P(X=k) = e⁻λ λᵏ / k!`

## 6. Variance and Standard Deviation

Population variance:

`σ² = Σ(xᵢ−μ)² / N`

Sample variance:

`s² = Σ(xᵢ−x̄)² / (n−1)`

Standard deviation:

`σ = √σ²`

Variance measures squared spread; standard deviation expresses spread in the original units.

## 7. Covariance and Correlation

Covariance:

`Cov(X,Y) = Σ[(xᵢ−x̄)(yᵢ−ȳ)] / (n−1)`

Pearson correlation:

`r = Cov(X,Y)/(σₓσᵧ)`

`−1 ≤ r ≤ 1`.

Correlation describes linear association and does not by itself prove causation.

## 8. Z-score

`z = (x−μ)/σ`

A z-score expresses an observation's distance from the mean in standard-deviation units.

## 9. Hypothesis Testing

Null hypothesis: `H₀`.

Alternative hypothesis: `H₁` or `Hₐ`.

Significance level: `α`, commonly `0.05`.

For a one-sample t-test:

`t = (x̄−μ₀)/(s/√n)`

A p-value measures how extreme the observed result is under H₀ and the test assumptions. A common rule is `p < α` → reject H₀; otherwise fail to reject H₀. Failing to reject H₀ does not prove it true.

## 10. Confidence Intervals

For a mean using an appropriate t procedure:

`x̄ ± t* × (s/√n)`

A 95% confidence interval refers to the long-run coverage of the procedure under its assumptions, not a 95% probability that a fixed parameter lies inside one computed interval.

## 11. Five-number Summary

Minimum, Q1, median, Q3, maximum.

Interquartile range:

`IQR = Q3 − Q1`

A common box-plot rule flags potential outliers below `Q1 − 1.5×IQR` or above `Q3 + 1.5×IQR`.

## Machine Learning connection

`Statistics → EDA → Feature Engineering → Modeling → Evaluation → Experimentation`

These mathematical concepts provide the foundation for understanding data and evaluating Machine Learning models.
