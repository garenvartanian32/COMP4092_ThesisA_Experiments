def calc_move(self, c):
        # first get local variables the same as battle.rules file so parser can interpret.
        AGI = c.stats['AGI']
        INT = c.stats['INT']
        STR = c.stats['STR']
        #STA = c.stats['STA']
        #print('calc move : self.rules.all_rules[hit_min] = ', self.rules.all_rules['hit_min'])
        #print('calc move : self.rules.all_rules[hit_max] = ', self.rules.all_rules['hit_max'])
        #print('calc move :  = self.rules.all_rules[hit_limit]', self.rules.all_rules['hit_limit'])
        hit_min   = float(self.rules.all_rules['hit_min'])
        
        hit_AGI_mult   = float(self.rules.all_rules['hit_AGI_mult'])
        hit_INT_mult   = float(self.rules.all_rules['hit_INT_mult'])
        hit_AGI_add   = float(self.rules.all_rules['hit_AGI_add'])
        hit_INT_add   = float(self.rules.all_rules['hit_INT_add'])
        hit_overall_add   = float(self.rules.all_rules['hit_overall_add'])
        
        #  hit_max = round(INT/2) + round(AGI/2) + 1
        hit_max = round(INT*(hit_INT_mult + hit_INT_add)) + round(AGI*(hit_AGI_mult + hit_AGI_add)) + hit_overall_add
        
        hit_limit = float(self.rules.all_rules['hit_limit']) 
        if hit_max > hit_limit:
            hit_max = hit_limit
        chance_hit = random.randint(hit_min,hit_max)
        
        dmg_min   = float(self.rules.all_rules['dmg_min'])
        #dmg_max   = eval(self.rules.all_rules['dmg_max'])
        calc_agi = round((AGI + float(self.rules.all_rules['dmg_AGI_add'])) * float(self.rules.all_rules['dmg_AGI_mult']))
        calc_int = round((INT + float(self.rules.all_rules['dmg_INT_add'])) * float(self.rules.all_rules['dmg_INT_mult']))
        calc_str = round((STR + float(self.rules.all_rules['dmg_STR_add'])) * float(self.rules.all_rules['dmg_STR_mult'])) 
        #print('TESTING CALC_MOVE : calc_agi', calc_agi, 'calc_int',calc_int ,'calc_str',calc_str )
        dmg_max = round((calc_agi + calc_int + calc_str) * float(self.rules.all_rules['dmg_overall_mult']) + float(self.rules.all_rules['dmg_overall_add']))
        #print('hit_min  =',hit_min  , 'hit_max = ',hit_max  )
        #print('dmg_min  =',dmg_min  , 'dmg_max = ',dmg_max  )
        amount_dmg = random.randint(dmg_min, dmg_max)
        
        if chance_hit > float(self.rules.all_rules['shot_crit_greater_than']):
            return 'Crit', amount_dmg * float(self.rules.all_rules['dmg_mult_crit'])
        elif chance_hit < float(self.rules.all_rules['shot_hit_greater_than']):
            return 'Miss', amount_dmg * float(self.rules.all_rules['dmg_mult_miss'])
        else:
            return 'Hit', amount_dmg * float(self.rules.all_rules['dmg_mult_hit'])