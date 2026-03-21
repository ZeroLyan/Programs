# This program will be a dark fantasy themed dungeon crawler.

# Libraries
import numpy as np
import os, time

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
        self.SPD = 7 # np.random.randint(1, 5)

# Helper Functions
def fight(player, enemy):
    os.system('clear')
    
    initiative_order = [[player.SPD, player.name], [enemy.SPD, enemy.name]]
    initiative_order.sort(reverse=True)
    print(initiative_order)
        
    print(f"{player.name} encountered a {enemy.name}. Fight!\n")
    print(f"{initiative_order[0][1]} is first\n")
    player_defending = False
    enemy_defendings = False
    time.sleep(1)

    while True:

         
        if enemy.SPD <= player.SPD:
            print(f"{player.name} HP: {player.HP}     {enemy.name} HP: {enemy.HP}\n")
            print("*" * 28)
            print("*  1. Fight     2. Defend  *")
            print("*  3. Items     4. Run     *")
            print("*" * 28, "\n\n")
            player_choice = int(input("What would you like to do: "))
            if 1 <= player_choice <= 4:
                break
        else:
            
            print(f"{enemy.name} chooses to attack {player.name}\n")
            if player_defending == True:

                player.HP -= enemy.ATK - player.DEF
                print(f"{enemy.name} dealt {enemy.ATK- player.DEF} damage to {player.name}\n")
            
            else:
            
                player.HP -= enemy.ATK
                print(f"{enemy.name} dealt {enemy.ATK} damage to {player.name}\n")

            print(f"{player.name} HP: {player.HP}     {enemy.name} HP: {enemy.HP}\n")
            
            print("*" * 28)
            print("*  1. Fight     2. Defend  *")
            print("*  3. Items     4. Run     *")
            print("*" * 28, "\n\n")
     
            player_choice = int(input("What would you like to do: "))
            if player_choice == 1:
                print(f"\n{player.name} attacks {enemy.name} for {player.ATK} damage\n")
                enemy.HP -= player.ATK
                time.sleep(1)
            if player_choice == 2:
                player_defending = True
                print(f"\n{player.name} is defending.\n")
                
            elif player_choice == 4:
                break

# Main Function
def main():
    
    player = Player("Jack")
    enemy = Enemy("Bandit")

    fight(player, enemy)

# Start of Program
if __name__ == '__main__':
    main()
