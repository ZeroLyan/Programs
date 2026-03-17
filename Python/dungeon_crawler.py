# This program will be a dark fantasy themed dungeon crawler.

# Libraries
import numpy as np

# Variables 


# Classes
class Player:
    def __init__(self, name):
        self.name = name
        self.HP = 10
        self.ATK = 2
        self.DEF = 1
        self.SPD = np.random.randint(1,5)

class Enemy:
    def __init__(self, name):
        self.name = name
        self.HP = 10
        self.ATK = 2
        self.DEF = 1
        self.SPD = np.random.randint(1, 5)

# Helper Functions
def fight(player, enemy):
    initiative_order = [[player.name, player.SPD], [enemy.name, enemy.SPD]]
    initiative_order.sort(reverse=True)
    print(initiative_order)

# Main Function
def main():
    
    player = Player("Jack")
    enemy = Enemy("Bandit")

    fight(player, enemy)

# Start of Program
if __name__ == '__main__':
    main()
