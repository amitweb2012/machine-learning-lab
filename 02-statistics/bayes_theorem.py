"""Bayes' theorem example: disease testing."""

# P(D): prevalence
# P(+|D): sensitivity
# P(+|not D): false-positive rate
p_disease = 0.01
p_positive_given_disease = 0.95
p_positive_given_no_disease = 0.05

p_positive = (
    p_positive_given_disease * p_disease
    + p_positive_given_no_disease * (1 - p_disease)
)

p_disease_given_positive = (
    p_positive_given_disease * p_disease / p_positive
)

print("P(positive) =", p_positive)
print("P(disease | positive) =", p_disease_given_positive)
