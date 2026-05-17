import random

class Battle:
    def __init__(self, rules):
        self.rules = rules

    def calc_move(self, c):
        # Assuming 'rules' is a dictionary with 'hit_max' key
        max_hit = self.rules['hit_max']

        # Assuming 'c' is a character and has a 'level' attribute
        level = c.level

        # Calculate damage
        damage = random.randint(1, max_hit) * level

        return damage