import numpy as np
import pandas as pd


class MonteCarloSimulation:

    def __init__(self):
        self.random_distribution = 'uniform'
        self.cum_prob = np.array([])
        # self.prob_col
        # self.out_col

    # Function to Accumulate the Probabilities
    def cumulate_probability(self, prob_col):
        # cum_prob = np.array([])
        self.cum_prob = np.append(self.cum_prob, prob_col[0])
        for i in range(1, len(prob_col)):
            self.cum_prob = np.append(self.cum_prob, self.cum_prob[i - 1] + prob_col[i])
        self.cum_prob[len(self.cum_prob) - 1] = 1.0
        return self.cum_prob

    # Function to Perform MCS
    # prob_col is the vector of probabilities
    # outcome_col is the vector of outcome values
    # n_trials is the number of iterations to simulate
    # random_distribution is the distribution to generate random numbers with values (0,1) either one of -
    #     'uniform'
    #     'normal'
    # returns the dataframe of simulation result with columns 'generated_number', 'resultant_number'
    def monte_carlo_simulation(self, prob_col, outcome_col, n_trials=100, random_distribution='uniform'):
        cumulative_prob = MonteCarloSimulation.cumulate_probability(self, prob_col)
        random_numbers = np.random.uniform(low=0.0, high=1.0, size=[n_trials])
        resultant_outcome = []
        n = len(prob_col)
        for rand in random_numbers:
            index = 0
        for i in range(n):
            if rand < cumulative_prob[i]:
                index = i
                break
        resultant_outcome.append(outcome_col[index])
        return_df = pd.DataFrame(columns=['generated_number', 'resultant_number'])
        return_df['generated_number'] = random_numbers
        return_df['resultant_number'] = resultant_outcome
        return return_df
