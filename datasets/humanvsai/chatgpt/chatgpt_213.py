import random

def create_character(name, race, char_class, stats, story, skills, inventory):
    character = {
        "Name": name,
        "Race": race,
        "Class": char_class,
        "Stats": stats,
        "Story": story,
        "Skills": skills,
        "Inventory": inventory
    }
    return character

# Example character traits
name = "Amador"
race = "Halfling"
char_class = "Priest"
stats = {
    "CON": 12,
    "STA": 4,
    "INT": 10,
    "STR": 0,
    "AGI": 5
}
story = "A brave person looking to fight evil in the dark forests of Divitie"
skills = ["Remove Curse", "Frost Ball", "Frost Bolt"]
inventory = ["5 gold", "stick", "leaf", "sword"]

# Generating a random character
random_stats = {
    "CON": random.randint(8, 14),
    "STA": random.randint(1, 7),
    "INT": random.randint(7, 13),
    "STR": random.randint(-3, 3),
    "AGI": random.randint(2, 8)
}
random_skills = random.sample(['Fireball', 'Ice Storm', 'Heal', 'Lightning Bolt', 'Teleport', 'Invisibility', 'Shield'], 3)
random_inventory = random.sample(['Gold', 'Food', 'Potion', 'Sword', 'Staff', 'Amulet', 'Armor'], 4)

random_character = create_character(name, race, char_class, random_stats, story, random_skills, random_inventory)
print(random_character)
