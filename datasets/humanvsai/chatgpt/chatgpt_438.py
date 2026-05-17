import pandas as pd

def get_less_than_constraints(prior_info):
    # Filter out zero-weighted pi
    prior_info = prior_info[prior_info['weight'] != 0]
    
    # Filter out pi that are not less than constraints
    less_than_constraints = prior_info[(prior_info['constraint_type'] == 'ineq') & (prior_info['weight'] > 0)]
    
    # Return the names of the pi that are less than constraints
    return pd.Series(less_than_constraints['name'])
