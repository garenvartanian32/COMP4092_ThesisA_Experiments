def calc_move(self, c):
    max_hit = eval(self.rules['hit_max'])
    damage = max_hit * c
    return damage