import os

def draw_meter(position, limit):
    # W ------||------ C
    left_track = "-" * (limit + position)
    right_track = "-" * (limit - position)
    print("\n" + "="*40)
    print(f"            W {left_track}||{right_track} C")
    print("="*40)
    print(f"Current Offset: {position} (Goal: {limit} or -{limit})")

def manual_battle():
    # Settings
    meter_limit = 5  # Number of 'wins' needed to kill the opponent
    position = 0      # 0 is the center
    
    while abs(position) < meter_limit:
        # Clear screen (optional, keeps the console clean)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("----- PATHFINDER 2E BATTLE TRACKER -----")
        draw_meter(position, meter_limit)
        
        print("\nCONTROLS:")
        print("[w] Wyeth Wins Roll (+1) | [c] Chief Wins Roll (-1)")
        print("[q] Quit Session")
        
        choice = input("\nAction: ").lower()
        
        if choice == 'w':
            position += 1
            print(">> Meter moves toward the Chief!")
            input("--->")
        elif choice == 'c':
            position -= 1
            print("<< Meter moves toward Wyeth!")
            input("--->")
        elif choice == 'q':
            break
        else:
            print("Invalid input. Use 'w' or 'c'.")
            input("--->")

    # Victory Check
    if position >= meter_limit:
        print("\n*** WYETH REACHED THE CHIEF! THE BOSS FALLS! ***")
    elif position <= -meter_limit:
        print("\n*** THE CHIEF REACHED WYETH! A GRIM END... ***")

if __name__ == "__main__":
    manual_battle()
