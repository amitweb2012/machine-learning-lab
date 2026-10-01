"""Descriptive statistics: mean, median, mode, range and quartiles."""
from statistics import mean, median, multimode


data = [10, 12, 12, 15, 18, 20, 20, 20, 25, 30]

print("Data:", data)
print("Mean:", mean(data))
print("Median:", median(data))
print("Mode(s):", multimode(data))
print("Minimum:", min(data))
print("Maximum:", max(data))
print("Range:", max(data) - min(data))
print("Count:", len(data))
