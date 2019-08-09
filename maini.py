# import numpy as np
import pandas as pd
from MonteCarloSimulation import MonteCarloSimulation

probability_table = pd.read_csv('probability_values.csv')
prob_col = probability_table.iloc[:, 0]
outcome_col = probability_table.iloc[:, 1]

mcs = MonteCarloSimulation()

df = mcs.monte_carlo_simulation(prob_col, outcome_col)
print("Expected Outcome is ", df['resultant_number'].mean())
