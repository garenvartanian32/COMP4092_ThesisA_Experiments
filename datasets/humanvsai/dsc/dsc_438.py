import pandas as pd

def less_than_pi_constraints(self):
    # Assuming self.prior_info is a pandas DataFrame with columns 'weight' and 'constraint_type'
    # where 'constraint_type' is 'less_than' for less than constraints
    less_than_constraints = self.prior_info[(self.prior_info['weight'] != 0) & (self.prior_info['constraint_type'] == 'less_than')]
    return less_than_constraints['pilbl']