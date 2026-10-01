"""Basic probability using counting and simulation."""
import random

# Classical probability: favorable outcomes / total outcomes
red_balls = 3
total_balls = 10
print("P(red) =", red_balls / total_balls)

# Simulation: estimate probability of rolling a 6
trials = 100_000
successes = sum(random.randint(1, 6) == 6 for _ in range(trials))
print("Estimated P(rolling 6) =", successes / trials)
