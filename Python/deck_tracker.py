import numpy as np


# Variables



# Helper Functions



def main():
    decks = ["Necrobloom", "Celes", "Iroh", "Sam and Frodo", 
             "Amareth", "Krenko", "Doctor Who", "Meren", "Edgar"]
    print('-' * 20 + " Magic The Gathering Decks " + '-' * 20)
    i = 0
    while i < (len(decks)):
        if i + 2 > len(decks):
            print(f"{i+1}. {decks[i]}")
            i = 500 
        else:
            print(f"{i+1}. {decks[i]:<10} {i+2:^3}. {decks[i+1]}")
            i += 2
    print('-' * 67)

if __name__ == "__main__":
    main()  