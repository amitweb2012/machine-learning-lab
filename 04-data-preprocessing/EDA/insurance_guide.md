# Insurance Dataset — EDA Learning Project

This project is a **first Exploratory Data Analysis (EDA) exercise** using an insurance dataset.

The goal is to learn how to inspect, clean, explore, visualize, transform, and statistically analyze a dataset **before learning Model Training and Model Evaluation**.

> **Important:** This project intentionally stops at EDA and statistical analysis. Machine Learning model training and evaluation are not included yet.

---

# 1. EDA Learning Flow

```text
                INSURANCE EDA
                     │
                     ▼
              Load Dataset
                     │
                     ▼
             Understand Data
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       shape       info      describe
          │
          ▼
       Data Quality
          │
      ┌───┴────┐
      ▼        ▼
   Missing   Duplicate
    values     values
      │
      ▼
   Univariate EDA
      │
 ┌────┴──────────┐
 ▼               ▼
Numerical     Categorical
 ▼               ▼
Histogram      Countplot
Boxplot
      │
      ▼
   Bivariate EDA
      │
 ┌────┴──────────────┐
 ▼                   ▼
Correlation       Category vs
                  Charges
      │
      ▼
 Feature Engineering
      │
      ▼
   BMI Category
      │
      ▼
 Statistical Analysis
      │
 ┌────┴──────────┐
 ▼               ▼
Pearson       Chi-square
correlation
```

---

# 2. Project Files

```text
insurance-eda/
│
├── insurance.csv
├── insurance.py
├── README.md
└── insurance_eda_cleaned.csv     # generated after running the script
```

---

# 3. Dataset

The input dataset is:

```text
insurance.csv
```

The main columns are:

| Column | Type | Meaning |
|---|---|---|
| `age` | Numerical | Age of the person |
| `sex` | Categorical | Sex |
| `bmi` | Numerical | Body Mass Index |
| `children` | Numerical | Number of children/dependents |
| `smoker` | Categorical | Smoking status |
| `region` | Categorical | Residential region |
| `charges` | Numerical | Insurance charges |

The target-like variable explored in this project is:

```text
charges
```

At this stage we are **not training a model**. We are simply trying to understand the data and relationships within it.

---

# 4. Section 1 — Load Dataset

Code:

```python
df = pd.read_csv("insurance.csv")
```

Purpose:

- Load the CSV file.
- Create a pandas DataFrame.
- Check whether the dataset is available and readable.

We also check:

```python
df.shape
```

to understand:

```text
(number of rows, number of columns)
```

---

# 5. Section 2 — Understand Data

We use:

```python
df.head()
df.tail()
df.shape
df.info()
df.describe()
df.columns
df.dtypes
```

## Why?

Before analyzing data, we need to answer:

- How many rows are there?
- How many columns?
- What are the column names?
- Which columns are numerical?
- Which columns are categorical?
- What are the minimum and maximum values?
- What are the mean and standard deviation?
- Are there suspicious values?

### Important functions

### `head()`

Shows the first rows.

```python
df.head()
```

### `tail()`

Shows the last rows.

```python
df.tail()
```

### `shape`

Returns:

```text
(rows, columns)
```

### `info()`

Shows:

- column names
- non-null counts
- data types
- memory information

### `describe()`

Provides descriptive statistics for numerical columns.

---

# 6. Section 3 — Data Quality

Data quality checks are performed before deeper analysis.

We check:

```text
Missing values
Duplicate rows
```

---

## 6.1 Missing Values

Code:

```python
df.isnull().sum()
```

This tells us how many missing values exist in each column.

We also calculate the percentage:

```python
df.isnull().mean() * 100
```

---

## 6.2 Duplicate Rows

Code:

```python
df.duplicated().sum()
```

This tells us how many complete duplicate rows exist.

For the cleaned EDA DataFrame:

```python
df_cleaned = df.copy()

df_cleaned.drop_duplicates(inplace=True)
df_cleaned.dropna(inplace=True)
```

### Important learning point

Removing duplicates and missing rows is a **data-cleaning decision**.

In a real project, we should understand why values are missing before automatically removing rows.

---

# 7. Section 4 — Numerical and Categorical Features

We identify the columns:

```python
numeric_columns = [
    "age",
    "bmi",
    "children",
    "charges"
]
```

and:

```python
categorical_columns = [
    "sex",
    "smoker",
    "region"
]
```

This distinction is important because different data types require different EDA techniques.

---

# 8. Section 5 — Univariate EDA

## What is Univariate Analysis?

**Uni = one**

We study one variable at a time.

Example:

```text
age
```

or:

```text
bmi
```

or:

```text
smoker
```

---

# 9. Numerical Univariate Analysis

For numerical variables we use:

```text
Histogram
KDE
Boxplot
```

---

## 9.1 Histogram

Example:

```python
sns.histplot(data=df_cleaned, x="age", kde=True)
```

A histogram helps answer:

- What is the distribution?
- Where are most observations?
- Is the distribution symmetric?
- Is it skewed?
- Are there unusual values?

---

## 9.2 KDE

KDE means:

**Kernel Density Estimation**

The KDE curve gives a smooth representation of the distribution.

Example:

```python
sns.histplot(data=df_cleaned, x="charges", kde=True)
```

---

## 9.3 Boxplot

Example:

```python
sns.boxplot(data=df_cleaned, x="charges")
```

A boxplot helps us understand:

```text
Minimum / lower boundary
Q1
Median
Q3
Maximum / upper boundary
Potential outliers
```

---

# 10. Categorical Univariate Analysis

For categorical variables we use:

```python
sns.countplot()
```

Example:

```python
sns.countplot(data=df_cleaned, x="smoker")
```

This helps answer:

> How many observations belong to each category?

For example:

```text
smoker

yes → count
no  → count
```

We also use:

```python
df_cleaned["smoker"].value_counts()
```

---

# 11. Section 6 — Five-Number Summary

For each numerical variable we calculate:

```text
Minimum
Q1
Median
Q3
Maximum
```

Example:

```python
minimum = df_cleaned["age"].min()
q1 = df_cleaned["age"].quantile(0.25)
median = df_cleaned["age"].median()
q3 = df_cleaned["age"].quantile(0.75)
maximum = df_cleaned["age"].max()
```

This is called the **Five-Number Summary**.

---

# 12. Section 7 — IQR and Outliers

IQR means:

**Interquartile Range**

Formula:

```text
IQR = Q3 - Q1
```

The commonly used IQR outlier boundaries are:

```text
Lower Bound = Q1 - 1.5 × IQR

Upper Bound = Q3 + 1.5 × IQR
```

The script calculates the number of potential outliers.

### Important

A statistical outlier does **not automatically mean an incorrect record**.

For example, a high insurance charge might be a genuine observation.

Therefore:

```text
Outlier ≠ Error
```

The purpose of this step is to **identify and investigate** unusual observations.

---

# 13. Section 8 — Bivariate EDA

## What is Bivariate Analysis?

**Bi = two**

We study the relationship between two variables.

Examples:

```text
age       vs charges
bmi       vs charges
smoker    vs charges
region    vs charges
```

---

# 14. Numerical Feature vs Charges

For numerical variables we use scatterplots.

Example:

```python
sns.scatterplot(
    data=df_cleaned,
    x="age",
    y="charges"
)
```

We do this for:

```text
age vs charges
bmi vs charges
children vs charges
```

Questions to ask:

- Is there a relationship?
- Is the relationship positive or negative?
- Is the relationship approximately linear?
- Are there unusual observations?
- Is the relationship weak or strong?

---

# 15. Categorical Feature vs Charges

For categorical variables, boxplots are useful.

Example:

```python
sns.boxplot(
    data=df_cleaned,
    x="smoker",
    y="charges"
)
```

We investigate:

```text
sex vs charges
smoker vs charges
region vs charges
```

This helps us compare the distribution of charges across categories.

---

# 16. Section 9 — Correlation Analysis

Correlation measures the strength and direction of a **linear relationship** between two numerical variables.

Pearson correlation ranges from:

```text
-1 to +1
```

General interpretation:

```text
+1 → strong positive linear relationship

 0 → no linear relationship

-1 → strong negative linear relationship
```

Correlation does **not** prove causation.

---

# 17. Correlation Matrix

The project calculates:

```python
df_cleaned[
    ["age", "bmi", "children", "charges"]
].corr()
```

Then visualizes it with a heatmap:

```python
sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm"
)
```

This lets us quickly inspect relationships between numerical variables.

---

# 18. Pearson Correlation

The project also calculates Pearson correlation using:

```python
pearsonr()
```

Example:

```python
r, p_value = pearsonr(
    df_cleaned["age"],
    df_cleaned["charges"]
)
```

The output contains:

```text
r
p-value
```

### `r`

Measures the strength and direction of the linear relationship.

### `p-value`

Used for statistical significance testing under the assumptions of the Pearson test.

---

# 19. Section 10 — Feature Engineering

Feature engineering means creating a useful new variable from existing information.

In this project we create:

```text
bmi_category
```

from:

```text
bmi
```

---

# 20. BMI Categories

The project uses:

```text
BMI < 18.5
    → Underweight

18.5 <= BMI < 25
    → Normal

25 <= BMI < 30
    → Overweight

BMI >= 30
    → Obesity
```

Implemented using:

```python
pd.cut()
```

The original:

```text
bmi
```

is kept as a continuous numerical variable.

The new:

```text
bmi_category
```

is a categorical feature.

---

# 21. Why Create BMI Category?

Compare:

```text
BMI = 31.7
```

with:

```text
BMI Category = Obesity
```

The continuous value preserves detailed numerical information.

The category provides an easier group-level interpretation.

This is an example of **feature engineering**.

---

# 22. Section 11 — Chi-Square Statistical Analysis

Chi-square tests are used to study relationships between categorical variables.

However:

```text
charges
```

is continuous.

Therefore, for this learning exercise, the project converts charges into four quartile groups:

```text
Q1
Q2
Q3
Q4
```

using:

```python
pd.qcut()
```

The Chi-square test then examines:

```text
categorical feature
        vs
charge quartile
```

---

# 23. Chi-Square Hypotheses

For each categorical feature:

### Null hypothesis H₀

There is no association between the categorical feature and charge quartile.

### Alternative hypothesis H₁

There is an association between the categorical feature and charge quartile.

We use:

```text
alpha = 0.05
```

Decision rule:

```text
p-value < 0.05
        ↓
Reject H₀

p-value >= 0.05
        ↓
Fail to Reject H₀
```

The script intentionally uses:

```text
"Fail to Reject H0"
```

rather than "Accept H0".

---

# 24. Important Chi-Square Learning Point

The Chi-square test in this project does **not** test the original continuous `charges` variable.

We first transform:

```text
charges
   ↓
Q1 / Q2 / Q3 / Q4
```

Therefore, the result should be interpreted as:

> Association between the categorical feature and insurance-charge quartile.

Not:

> Association between the categorical feature and the exact continuous insurance charge.

This distinction is important.

---

# 25. What This Project Does NOT Cover Yet

This project intentionally does not cover:

```text
Model Training
Model Prediction
Model Evaluation
```

Those are the next ML stages.

The future workflow will be:

```text
EDA
 ↓
X and y
 ↓
Train/Test Split
 ↓
Preprocessing
 ↓
Model Training
 ↓
Prediction
 ↓
Model Evaluation
```

Do not add those sections until the EDA concepts are comfortable.

---

# 26. Important EDA Concepts Learned

After completing this project, you should understand:

### Data understanding

```text
shape
head
tail
info
describe
dtypes
```

### Data quality

```text
missing values
duplicates
```

### Univariate analysis

```text
histogram
KDE
boxplot
countplot
```

### Descriptive statistics

```text
mean
median
minimum
maximum
Q1
Q3
IQR
standard deviation
```

### Outlier analysis

```text
IQR
Lower Bound
Upper Bound
```

### Bivariate analysis

```text
scatterplot
boxplot
```

### Correlation

```text
Pearson correlation
correlation matrix
heatmap
```

### Feature engineering

```text
BMI → BMI Category
```

### Statistical testing

```text
Chi-square
p-value
alpha
H0
H1
```

---

# 27. Installation

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn scipy
```

---

# 28. Run the Project

Place these files in the same directory:

```text
insurance.csv
insurance.py
README.md
```

Then run:

```bash
python insurance.py
```

The program will print statistical information and display the EDA charts.

It will also generate:

```text
insurance_eda_cleaned.csv
```

---

# 29. Suggested Learning Method

Don't just run the script.

For each section:

1. Run the code.
2. Look at the output.
3. Look at the graph.
4. Ask what the graph is telling you.
5. Change one parameter.
6. Run it again.
7. Explain the result in your own words.

For example, don't memorize:

```python
sns.histplot()
```

Instead understand:

> "I use a histogram because I want to understand the distribution of one numerical variable."

Similarly:

> "I use a scatterplot when I want to visually investigate the relationship between two numerical variables."

And:

> "I use Pearson correlation to quantify the strength and direction of a linear relationship."

That is the actual goal of this project.

---

# 30. Learning Roadmap After This Project

Once this EDA project is comfortable:

```text
                    EDA
                     │
                     ▼
                Statistics
                     │
                     ▼
             Feature Engineering
                     │
                     ▼
              Train/Test Split
                     │
                     ▼
              Model Training
                     │
                     ▼
             Model Evaluation
                     │
                     ▼
            Model Improvement
```

For now, focus on the **EDA box**.

---

# 31. Final EDA Checklist

Use this checklist while studying:

- [ ] Load dataset
- [ ] Understand rows and columns
- [ ] Check data types
- [ ] Check missing values
- [ ] Check duplicates
- [ ] Separate numerical/categorical features
- [ ] Create numerical histograms
- [ ] Understand KDE
- [ ] Create boxplots
- [ ] Create categorical countplots
- [ ] Understand five-number summary
- [ ] Calculate IQR
- [ ] Identify potential outliers
- [ ] Create scatterplots
- [ ] Compare categorical variables with charges
- [ ] Create correlation matrix
- [ ] Understand Pearson correlation
- [ ] Understand p-value
- [ ] Create BMI category
- [ ] Understand feature engineering
- [ ] Understand Chi-square
- [ ] Understand H₀ and H₁
- [ ] Understand alpha
- [ ] Understand "Reject H₀"
- [ ] Understand "Fail to Reject H₀"

---

## Next stage

After you're comfortable with all of the above, the natural next project step is **not immediately a complicated model**.

We can take this same `insurance.csv` and learn:

```text
X and y
   ↓
Train/Test Split
   ↓
What is a model?
   ↓
Linear Regression
   ↓
Fit
   ↓
Predict
   ↓
MAE / MSE / RMSE / R²
```

That will make the transition from **EDA → Machine Learning** much easier.
