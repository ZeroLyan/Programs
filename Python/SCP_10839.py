# SCP-10839 - "The Digital Oracle" is a terminal located in an impossible site that never existed. It holds knowledge on all current SCP's in existence.

import time
import random
import os


# Helper Functions
def type_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay + random.uniform(0, 0.02))
    print()

def pause(a=0.2, b=0.6):
    time.sleep(random.uniform(a, b))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def spinner(duration=3, message=" > Loading"):
    symbols = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        print(f"\r{message}... {symbols[i % len(symbols)]}", end='', flush=True)
        time.sleep(0.1)
        i += 1
    print("\r" + " " * (len(message) + 10) + "\r", end='', flush=True)

def progress_bar(total=20, duration=2, message=" > Processing"):
    for i in range(total + 1):
        percent = (i / total) * 100
        bar = '#' * i + '-' * (total - i)
        print(f"\r{message}: [{bar}] {percent:.0f}%", end='', flush=True)
        time.sleep(duration / total)
    print()

def glitch_loading(message = " > Corrupted Data Detected..."):
    type_print(message, delay=0.05)
    type_print(" > Attempting to recover...", delay=0.05)
    spinner(5, " > Recovering")
    for _ in range(3):
        glitch_symbols = ['#', '-', ' ', '@', '%', '&']
        bar = ''.join(random.choice(glitch_symbols) for _ in range(20))
        print(f"\r > [{bar}]", end='', flush=True)
        time.sleep(0.4)
    print("\r" + " " * 22 + "\r", end='', flush=True)


# Boot Animation Functions
def start_up():
    clear_screen()
    type_print(" " * 25 + "SCP FOUNDATION TERMINAL" + " " * 25)
    type_print("_" * 80)
    type_print(" > Powering on...")
    spinner(4, " > Booting")
    progress_bar(30, 3, " > Initializing Systems")
    glitch_loading()


def login_screen():
    clear_screen()

    
    pause()

def main():
    start_up()

if __name__ == "__main__":
    main()