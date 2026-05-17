import ast
import operator

def calculate_damage(battle_rules, attack_power, defense_power, critical_chance):
    max_hit = ast.literal_eval(battle_rules['hit_max'])
    min_hit = ast.literal_eval(battle_rules['hit_min'])
    critical_multiplier = ast.literal_eval(battle_rules['critical_multiplier'])
    damage_multiplier = ast.literal_eval(battle_rules['damage_multiplier'])
    
    hit_chance = min(max_hit, (attack_power / defense_power)) * (1 + critical_chance)
    damage = (damage_multiplier * attack_power * hit_chance) / defense_power
    
    if hit_chance == max_hit:
        damage *= critical_multiplier
    
    return damage
