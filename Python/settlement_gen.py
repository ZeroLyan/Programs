# This program will incremently generate a settlement of a given size for Pathfiner 2e

import json, random

# Classes for settlement generation

class NPC:
    def __init__(self, ancestry, gender, age, name, npc_id):
        self.id = npc_id
        self.name = name
        self.ancestry = ancestry
        self.age = age
        self.gender = gender

        # Core
        self.house_id = None
        self.job = None

        # Importance tiers
        self.importance = "background"  # background, important, key

        # Expandable details
        self.relationships = []
        self.traits = []
        self.secrets = []

# Dictionaries for settlements
SETTLEMENT_SIZES = {

    "hamlet": {
        "category": "hamlet",
        "population": (10,30),
        "max_level" : 1,
        "description": "Tiny cluster of homes, minimal services"
    },

    "village": {
        "category": "village",
        "population": (30,100),
        "max_level" : 2,
        "description": "Small rural community with basic trade"
    },

    "town": {
        "category": "town",
        "population": (100,1000),
        "max_level" : 4,
        "description": "Regional hub with multiple trades"
    },

    "city": {
        "category": "city",
        "population": (1000,10000),
        "max_level" : 7,
        "description": "Major enconomic and political center"
    },

    "metropolis": {
        "category": "metropolis",
        "population": (10000,100000),
        "max_level" : 10,
        "description": "Massive urban center of power."
    }
}

SETTLEMENT_FEATURES = {
    "hamlet": ["small farm", "village well"],
    "village": ["tavern", "general store", "shrine"],
    "town": ["blacksmith", "apothecary", "guard post"],
    "city": ["temple", "market square", "guild hall"],
    "metropolis": ["castle", "university", "theater"]
}

# Functions to build the settlement
def get_size():
    print("Select settlement size:")
    for i, size in enumerate(SETTLEMENT_SIZES.keys(), 1):
        print(f"{i}. {size.title()} - {SETTLEMENT_SIZES[size]['description']}")
    
    while True:
        choice = input("Enter the number corresponding to the settlement size: ")
        if choice.isdigit() and 1 <= int(choice) <= len(SETTLEMENT_SIZES):
            return list(SETTLEMENT_SIZES.keys())[int(choice) - 1]
        else:
            print("Invalid choice. Please try again.")

def get_population(size):
    pop_range = SETTLEMENT_SIZES[size]["population"]
    return random.randint(pop_range[0], pop_range[1])

def get_features(size):
    features = []
    for key in SETTLEMENT_SIZES.keys():
        if key == size:
            features.extend(SETTLEMENT_FEATURES[key])
            break
        features.extend(SETTLEMENT_FEATURES[key])   
    return features

def estimate_buildings(population):
    return {
        "homes": population // 4,
        "shops": max(1, population // 25),
        "special": max(1, population // 100)  
    }

def get_ancestries():
    all_ancestries = ["Human", "Elf", "Dwarf", "Halfling", "Gnome", "Goblin", "Orc", "Leshy"]

    print("Which ancestries are present in the settlement? (Enter numbers separated by commas)")
    for i, ancestry in enumerate(all_ancestries, 1):
        print(f"{i}. {ancestry}")

    choices = list(map(int, input("Your choices: ").split(",")))
    selected_ancestries = [all_ancestries[i - 1] for i in choices if 1 <= i <= len(all_ancestries)]
    return selected_ancestries

def generate_name(ancestry, gender):


def generate_pop(size):

    npcs = []

    ancestries = get_ancestries()

    for i in range(size):

        npc = NPC(
            ancestry = random.choice(ancestries),
            gender = random.choice(["Male", "Female", "Non-Binary"])
            age = generate_age()
            name = generate_name(),
            npc_id = i,
        )

        npcs.append(npc)
    return npcs

def main():
    size = get_size()
    for key, value in SETTLEMENT_SIZES[size].items():
        print(f"{key.title()}: {value}")
    
    pop_size = get_population(size)
    print(pop_size)

    feats = get_features(size)
    print("Features:")
    for feat in feats:
        print(f"- {feat}")

    buildings = estimate_buildings(pop_size)
    for key, value in buildings.items():
        print(f"{key.title()}: {value}")

    ancestries = get_ancestries()
    print("Ancestries present:")
    for ancestry in ancestries:
        print(f"- {ancestry}")

if __name__ == "__main__":
    main()