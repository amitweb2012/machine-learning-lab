"""Conditional probability: P(A|B) = P(A and B) / P(B)."""

# From 100 students: 40 study Python, 25 study both Python and ML,
# and 50 study Machine Learning.
p_python_and_ml = 25 / 100
p_ml = 50 / 100

p_python_given_ml = p_python_and_ml / p_ml
print("P(Python | ML) =", p_python_given_ml)

# Equivalent count interpretation: 25 of the 50 ML students also study Python.
print("25 / 50 =", 25 / 50)
