"""One-sample and two-sample hypothesis testing examples."""
import numpy as np
from scipy import stats

# H0: mean delivery time = 30 minutes
# H1: mean delivery time != 30 minutes
sample = np.array([28, 31, 29, 35, 32, 27, 30, 34, 31, 33], dtype=float)
t_stat, p_value = stats.ttest_1samp(sample, popmean=30)
print("One-sample t-test statistic:", t_stat)
print("p-value:", p_value)
print("Decision at alpha=0.05:", "Reject H0" if p_value < 0.05 else "Fail to reject H0")

# Compare two independent groups.
group_a = [72, 75, 70, 68, 74, 77]
group_b = [80, 82, 79, 85, 81, 83]
t_stat2, p_value2 = stats.ttest_ind(group_a, group_b, equal_var=False)
print("\nWelch two-sample t-test statistic:", t_stat2)
print("p-value:", p_value2)
