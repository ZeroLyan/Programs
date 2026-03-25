# This program will be a dark fantasy themed dungeon crawler.

# Libraries
import numpy as np
import os, time

# Variables 


# Classes

# Class for the Player
class Player:
    
    # Function to initiate the player
    def __init__(self, name):
        self.name = name
        self.HP = 10
        self.ATK = 2
        self.DEF = 1
        self.SPD = np.random.randint(1,5)
        self.items = []

    # Funtion to print the players stats
    def print_stats(self):
        print("\n\n" + "*" * 29 + f"[Stats]" + "*" * 29)
        print(" " * 3 + '_' * 50 )
        print(" " * 2 + f"|  Name: {self.name}")
        for k, v in vars(self).items():
            if isinstance(v, int):
                print(" " * 2 + f"|  {k}: {v}")
    
    #Function to print players inventory
    def print_inventory(self):
        print("\n\n" + "*" * 27 + f"[Inventory]" + "*" * 27)
        print(" " * 3 + '_' * 20 + f"{self.name}'s Inventory" + '_' * 20)
        for items in self.items:
            print(" " * 2 + f"|  {items[0]}x {items[1]}")
    
    # Function to add items to the players inventory    
    def add_item(self, quant, name):
         self.items.append([quant, name])

# Class for the Enemies
class Enemy:

    # Function to initiate the enemies
    def __init__(self, name):
        self.name = name
        self.HP = 10
        self.ATK = 2
        self.DEF = 1
        self.SPD = 7 # np.random.randint(1, 5)

# Helper Functions
def start_game():
    
    menu_choice = main_menu()

    if menu_choice == '1' or menu_choice.title() == 'Play':
        #os.system("clear")
        player = create_char()
        game_loop(player)      
          
    return menu_choice

def game_loop(player):
    fight(player, enemy=Enemy('Bandit'))

def create_char():

    equipment = ["Sword", "Shield", "Boots", "Armor"]

    print('*' * 24 + f"[Create Your Character]" + '*' * 24)
    print(" " * 3 + "_" * 57)
    
    player_name = input(" " * 2 + "|  Name: ")
    print(" " * 2 + f"|  Are you sure you want to be called {player_name}? y/n")
    
    name_check = input(" " * 2 + "|  Answer: ")
    if name_check == 'n':
        player_name = input(" " * 2 + "|  Name: ")
    
    print(" " * 2 + f"|  Choose a starting equip: 1.{equipment[0]} 2.{equipment[1]} 3.{equipment[2]} 4.{equipment[3]}")
    
    chosen_item = int(input(" " * 2 + f"|  Equip: "))
    player = Player(player_name)
    player.add_item(1, equipment[chosen_item - 1])
    
    print(" " * 2 + f"|  Welcome {player.name}! Hope you brought your lucky {player.items[0][1]}!") 
    print(" " * 2 + "|  Time to enter the dungeon.")
    print(" " * 2 + "|  Press any key to continue: ", end='')
    
    player.print_stats()
    player.print_inventory()
    pause = input()
    
    if chosen_item == 1:
        player.ATK += 2
    elif chosen_item == 2:
        player.DEF += 1
    elif chosen_item == 3:
        player.SPD += 2
    elif chosen_item == 4:
        player.HP += 5
    
    return player

def main_menu():
    print(f"{'Dungeon Fighter':^70}")
    print("\n")
    print(f"{'1. Play':^70}")
    print(f"{"2. Quit":^70}")
    menu_choice = input(f"\n{"Pick an option: ":>43}")
    return menu_choice


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
    
    '''player = Player("Jack")
    enemy = Enemy("Bandit")

    fight(player, enemy)'''
    while True:
        
        quit = start_game()
        if quit == '2' or quit.title() == "Quit":
            break

# Start of Program
if __name__ == '__main__':
    main()
