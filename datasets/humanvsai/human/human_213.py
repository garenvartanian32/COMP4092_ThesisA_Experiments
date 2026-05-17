def generate_random_character(self):
        name = self.create_name()
        ch_class = self.classes.get_random_choice()
        race = self.races.get_random_choice()
        stats = self.random_stats(self.stats.dat, race, ch_class)
        skills = []
        story = self.stories.get_random_choice()
        inventory = [str(random.randint(21,29)) + ' gold']
        
        # pick random stuff here 
        for _ in range(3):
            inventory.append(self.inventory.get_random_choice())
        for _ in range(3):
            skills.append(self.skills.get_random_choice())
        return Character(name, race, ch_class, stats, skills, story, inventory)