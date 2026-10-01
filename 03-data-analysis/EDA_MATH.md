# 📐 EDA Mathematical Explanation

## 1. Mean

**x̄ = Σxᵢ / n**

The mean is the arithmetic center of numerical observations and can be influenced by extreme values.

## 2. Median and Quartiles

After sorting observations:

- Q1 = 25th percentile
- Q2 = median = 50th percentile
- Q3 = 75th percentile

## 3. Range and IQR

**Range = Maximum − Minimum**

**IQR = Q3 − Q1**

IQR describes the spread of the middle 50% of observations.

## 4. Variance and Standard Deviation

Population variance:

**σ² = Σ(xᵢ − μ)² / N**

Sample variance:

**s² = Σ(xᵢ − x̄)² / (n − 1)**

Standard deviation:

**σ = √σ²**

## 5. Five-number Summary and Outliers

**Minimum, Q1, Median, Q3, Maximum**

Common box-plot fences:

**Lower = Q1 − 1.5 × IQR**

**Upper = Q3 + 1.5 × IQR**

Values outside these fences are potential outliers, not automatically errors.

## 6. Z-score

**z = (x − μ) / σ**

A z-score describes distance from the mean in standard-deviation units.

## 7. Covariance

**Cov(X,Y) = Σ[(xᵢ − x̄)(yᵢ − ȳ)] / (n − 1)**

Positive covariance indicates that variables tend to move together; negative covariance indicates opposite movement. Magnitude depends on measurement units.

## 8. Pearson Correlation

**r = Cov(X,Y) / (sₓsᵧ)**

`r` lies between -1 and +1. It measures linear association, not causation.

## 9. Distribution and Frequency

For a histogram bin:

**proportion = observations in bin / total observations**

A density histogram represents probability density; total area is approximately 1.

## 10. Skewness

A standardized third central moment is:

**γ₁ = E[(X − μ)³] / σ³**

Positive skew indicates a longer right tail; negative skew indicates a longer left tail. Zero skewness does not guarantee normality.

## 11. Categorical Frequency

**relative frequency = count(category) / total count**

**percentage = 100 × count(category) / total count**

For example, 90 churned customers out of 300 gives a 30% churn rate.

## 12. Grouped Analysis

A grouped mean is:

**x̄_group = Σxᵢ / n_group**

Grouped summaries help compare categories, but descriptive differences alone do not establish causality or statistical significance.

## 13. Why EDA Before ML?

EDA helps reveal:

1. Missing values
2. Duplicates
3. Invalid ranges
4. Extreme values
5. Skewed distributions
6. Category imbalance
7. Feature relationships
8. Possible leakage
9. Data-quality problems
10. Candidate transformations

The practical flow is:

**Raw Data → EDA → Cleaning → Feature Engineering → Modeling → Evaluation**

## 14. Interpreting EDA

If customers with lower satisfaction also show higher churn frequency, this is an observed association. It does not prove that low satisfaction causes churn. Other variables, selection effects, measurement effects, or reverse relationships may contribute.

## 15. EDA Checklist

### Structure
- Shape
- Columns
- Data types
- Target definition

### Quality
- Missing values
- Duplicates
- Invalid values
- Unexpected categories

### Numerical
- Mean
- Median
- Standard deviation
- Quartiles
- IQR
- Skewness
- Histograms
- Box plots

### Categorical
- Frequency
- Percentage
- Category balance
- Target rate by category

### Relationships
- Scatter plots
- Grouped summaries
- Covariance
- Correlation
- Heatmap

### ML preparation
- Leakage checks
- Transformations
- Encoding
- Scaling
- Outlier strategy

## Connection to Statistics

`02-statistics` establishes the mathematics; `03-data-analysis` applies it to a dataset.

**Mathematics → Statistics → EDA → Machine Learning**
