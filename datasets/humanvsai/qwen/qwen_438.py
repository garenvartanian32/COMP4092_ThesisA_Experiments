def less_than_pi_constraints(self):
    filtered_df = self.pi[(self.pi['rel'] == '<') & (self.pi['wt'] != 0)]
    return filtered_df['pilbl']