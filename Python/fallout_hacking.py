# This program will simulate the fallout hacking minigame.
import numpy as np
import os
import time

# Variables for the game
password_list = ["Riot", "Mass", "Lust", "Role", "Noon", "Moon", "Drag", "Brag", "Bags", "Mean", "Bean", "Band", "Swam"
                 , "Pool", "Moor", "More", "Jazz", "Razz", "Maze", "Daze", "Hate"]
char_list = ['(', ')', '[', ']', '{', '}', '<', '>', '!', '@', '#', '$', '%', '^', '&', '-', '_', '+', '=', '|',
            '/', ':', ';', '"', '\'', '?', '.', ',']

string_list1 = []
string_list2 = []

# Helper Functions
def play_game():
    attempts = 4
    password, str_list1, str_list2 = gen_string_list()
    correct_letters = how_many_right(password, "Batman")
    guesses = []

    while True:
        create_layout(password, attempts, str_list1, str_list2, correct_letters, guesses)
        player_guess = input(">").title()
        if player_guess == password:
            print("You win!")
            return False
        else:
            print("Incorrect password!")
            time.sleep(1)
            attempts -= 1
            correct_letters = how_many_right(password, player_guess)
            guesses.append(player_guess)
        if attempts == 0:
            print("LOCKED OUT! CALL YOUR ADMINISTRATOR!")
            time.sleep(2)
            break

def gen_string_list():
    password = np.random.choice(password_list)
    password_list.remove(password)
    idx1_pos = np.random.randint(0, 17)
    idx2_pos = np.random.randint(0, 17)
    while idx1_pos == idx2_pos:
        idx1_pos = np.random.randint(0, 17)
    counter = 0
    for i in range(17):
        rand_chars1 = ''
        rand_chars2 = ''
        picked_word = 'Batman'
        for j in range(12):
            rand_chars1 += np.random.choice(char_list)
            rand_chars2 += np.random.choice(char_list)
        if counter == idx1_pos:
            idx_pos3 = np.random.randint(0, len(rand_chars1) - 3)
            rand_chars1 = rand_chars1[:idx_pos3] + password + rand_chars1[idx_pos3 + len(password):]
            counter = 500

        elif counter == idx2_pos:
            idx_pos3 = np.random.randint(0, len(rand_chars1) - 3)
            rand_chars2 = rand_chars2[:idx_pos3] + password + rand_chars2[idx_pos3 + len(password):]
            counter = 500
        else:
            word_roll = np.random.randint(1, 10)
            if 1 <= word_roll <= 5:
                pos_roll = np.random.randint(1, 10)
                picked_word = np.random.choice(password_list)
                password_list.remove(picked_word)
                idx_pos1 = np.random.randint(0, len(rand_chars1) - 3)
                idx_pos2 = np.random.randint(0, len(rand_chars2) - 3)
                if 1 <= pos_roll < 4:
                    rand_chars1 = rand_chars1[:idx_pos1] + picked_word + rand_chars1[
                        idx_pos1 + len(picked_word):]

                elif 4 <= pos_roll <= 5:
                    picked_word2 = np.random.choice(password_list)
                    password_list.remove(picked_word2)
                    rand_chars1 = rand_chars1[:idx_pos1] + picked_word + rand_chars1[
                        idx_pos1 + len(picked_word):]
                    rand_chars2 = rand_chars2[:idx_pos2] + picked_word2 + rand_chars2[
                        idx_pos2 + len(picked_word2):]

                elif 5 < pos_roll <= 10:
                    rand_chars2 = rand_chars2[:idx_pos2] + picked_word + rand_chars2[
                        idx_pos2 + len(picked_word):]
            counter += 1

        string_list1.append(rand_chars1)
        string_list2.append(rand_chars2)
    return password, string_list1, string_list2

def how_many_right(password, player_guess):
    checker = 0
    for i in range(len(password)):
        if password[i] == player_guess[i]:
            checker += 1
    return checker

def create_layout(password, attempts, string_list1, string_list2, correct_letters, guesses):
    hex_start = "0xF964"
    hex_to_dec = int(hex_start, 16)
    os.system("clear")
    print(password)
    print(correct_letters)
    print("ROBCO INDUSTRIES (TM) TERMLINK PROTOCOL")
    print("!!! WARNING: LOCKOUT IMMINENT !!!")
    print(f"\n {attempts} ATTEMPT(S) LEFT: {'#' * attempts}")
    for y in range(17):
        if attempts == 4:
            if y == 16:
                print(f"0x{hex_to_dec:X} {string_list1[y]}  0x{hex_to_dec + 204:X} {string_list2[y]}", end=' ')
            else:
                print(f"0x{hex_to_dec:X} {string_list1[y]}  0x{hex_to_dec + 204:X} {string_list2[y]}")
        elif attempts == 3:
            if y == 16:
                print(f"0x{hex_to_dec:X} {string_list1[y]}  0x{hex_to_dec + 204:X} {string_list2[y]}", end=' ')

            elif y == 14:
                print(f"0x{hex_to_dec:X} {string_list1[y]}  0x{hex_to_dec + 204:X} {string_list2[y]} >{how_many_right(password, guesses[0])}/4 correct")

            elif y == 13:
                print(f"0x{hex_to_dec:X} {string_list1[y]}  0x{hex_to_dec + 204:X} {string_list2[y]} >Entry denied")

            elif y == 12:
                print(f"0x{hex_to_dec:X} {string_list1[y]}  0x{hex_to_dec + 204:X} {string_list2[y]} >{guesses[0].upper()}")

            else:
                print(f"0x{hex_to_dec:X} {string_list1[y]}  0x{hex_to_dec + 204:X} {string_list2[y]}")
        elif attempts == 2:
            if y == 16:
                print(f"0x{hex_to_dec:X} {string_list1[y]}  0x{hex_to_dec + 204:X} {string_list2[y]}", end=' ')

            elif y == 14:
                print(f"0x{hex_to_dec:X} {string_list1[y]}  0x{hex_to_dec + 204:X} {string_list2[y]} >{how_many_right(password, guesses[0])}/4 correct")

            elif y == 13:
                print(f"0x{hex_to_dec:X} {string_list1[y]}  0x{hex_to_dec + 204:X} {string_list2[y]} >Entry denied")

            elif y == 12:
                print(f"0x{hex_to_dec:X} {string_list1[y]}  0x{hex_to_dec + 204:X} {string_list2[y]} >{guesses[0].upper()}")

            elif y == 11:
                print(f"0x{hex_to_dec:X} {string_list1[y]}  0x{hex_to_dec + 204:X} {string_list2[y]} >{how_many_right(password, guesses[1])}/4 correct")

            elif y == 10:
                print(f"0x{hex_to_dec:X} {string_list1[y]}  0x{hex_to_dec + 204:X} {string_list2[y]} >Entry denied")

            elif y == 9:
                print(f"0x{hex_to_dec:X} {string_list1[y]}  0x{hex_to_dec + 204:X} {string_list2[y]} >{guesses[1].upper()}")

            else:
                print(f"0x{hex_to_dec:X} {string_list1[y]}  0x{hex_to_dec + 204:X} {string_list2[y]}")
        elif attempts == 1:
            if y == 16:
                print(f"0x{hex_to_dec:X} {string_list1[y]}  0x{hex_to_dec + 204:X} {string_list2[y]}", end=' ')

            elif y == 14:
                print(
                    f"0x{hex_to_dec:X} {string_list1[y]}  0x{hex_to_dec + 204:X} {string_list2[y]} >{how_many_right(password, guesses[0])}/4 correct")

            elif y == 13:
                print(f"0x{hex_to_dec:X} {string_list1[y]}  0x{hex_to_dec + 204:X} {string_list2[y]} >Entry denied")

            elif y == 12:
                print(
                    f"0x{hex_to_dec:X} {string_list1[y]}  0x{hex_to_dec + 204:X} {string_list2[y]} >{guesses[0].upper()}")

            elif y == 11:
                print(
                    f"0x{hex_to_dec:X} {string_list1[y]}  0x{hex_to_dec + 204:X} {string_list2[y]} >{how_many_right(password, guesses[1])}/4 correct")

            elif y == 10:
                print(f"0x{hex_to_dec:X} {string_list1[y]}  0x{hex_to_dec + 204:X} {string_list2[y]} >Entry denied")

            elif y == 9:
                print(
                    f"0x{hex_to_dec:X} {string_list1[y]}  0x{hex_to_dec + 204:X} {string_list2[y]} >{guesses[1].upper()}")

            elif y == 8:
                print(
                    f"0x{hex_to_dec:X} {string_list1[y]}  0x{hex_to_dec + 204:X} {string_list2[y]} >{how_many_right(password, guesses[2])}/4 correct")

            elif y == 7:
                print(f"0x{hex_to_dec:X} {string_list1[y]}  0x{hex_to_dec + 204:X} {string_list2[y]} >Entry denied")

            elif y == 6:
                print(
                    f"0x{hex_to_dec:X} {string_list1[y]}  0x{hex_to_dec + 204:X} {string_list2[y]} >{guesses[2].upper()}")

            else:
                print(f"0x{hex_to_dec:X} {string_list1[y]}  0x{hex_to_dec + 204:X} {string_list2[y]}")

        hex_to_dec += 12

def main():
   play_game()

if __name__ == "__main__":
    main()
