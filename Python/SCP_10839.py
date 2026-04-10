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

def progress_bar(total=20, duration=5, message=" > Processing"):
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

def print_ascii_logo():
    clear_screen()
    # Function to print out the ascii art header for the terminal using the SCP Foundation logo using type print
    header = r"""
    .-----------------------------------------------------------------------------.
    |  ____                                              ###########              |
    | / ___|  ___  ___ _   _ _ __ ___                   ##         ##             |
    | \___ \ / _ \/ __| | | | '__/ _ \              m###*     m     *###m         |
    |  ___) |  __/ (__| |_| | | |  __/_           ##*     ..#####,,     *##       |
    | |____/ \___|\___|\__,_|_|  \___(_)        m##    .#############,    ##m     |
    |   ____            _        _             ##    .###     #     ###,    ##    |
    |  / ___|___  _ __ | |_ __ _(_)_ __       m#    ###     #####     ###    #m   |
    | | |   / _ \| '_ \| __/ _` | | '_ \      ##   .##       '#'      ###,   ##   |
    | | |__| (_) | | | | || (_| | | | | |_    ##   ###   wwwww wwwww   ###   ##   |
    |  \____\___/|_| |_|\__\__,_|_|_| |_(_)   ##   '##  w####   ####w  ##*   ##   |
    |  ____            _            _       ,#*     *###*' *     * '*####     '#, |
    | |  _ \ _ __ ___ | |_ ___  ___| |_      ##,   *'*###,         ,###'`'   ,##  |
    | | |_) | '__/ _ \| __/ _ \/ __| __|      *##       '*#########*'       ##'   |
    | |  __/| | | (_) | ||  __/ (__| |_ _       ##.,#m                 m#,.##     |
    | |_|   |_|  \___/ \__\___|\___|\__(_)       *'  *#####m     m#####*  '*      |
    |                                                    '*#######*'              |
    '-----------------------------------------------------------------------------'
    """
    type_print(header, delay=0.000000001) 

def fast_fetch():
    # Simulate what fastfetch does in a linux terminal by displaying system information
    type_print(" > Fetching system information...")
    time.sleep(1)
    system_info = { 
        "OS": "SCP-OS 1.0",
        "Kernel": "Oracle-Kernel 5.4",
        "Uptime": f"{random.randint(1, 10)} days, {random.randint(0, 23)} hours, {random.randint(0, 59)} minutes, {random.randint(0, 59)} seconds",
        "CPU": "Intel Core i15-10839K @ 3.7GHz",
        "RAM": "1028GB DDR4",
        "Storage": "2PB NVMe SSD",
        "Network": "Ethernet - 1Tbps"
    }
    for key, value in system_info.items():
        type_print(f" > {key}: {value}")
        time.sleep(0.5)
# Boot Animation Functions
def boot_sequence():
    # Simulate a boot sequence with various system checks
    type_print(" > Initializing operating system...")
    spinner(3, " > Loading kernel")
    type_print(" > Checking hardware components...")
    fast_fetch()
    progress_bar(20, 4, " > Running diagnostics")
    type_print(" > Hardware check complete. No issues found.")
    type_print(" > Loading user interface...")
    spinner(4, " > Starting terminal services")
    type_print(" > Terminal ready.")


def start_up():
    print_ascii_logo()
    type_print(" > Powering on...")
    spinner(4, " > Loading Boot Sequence")
    boot_sequence()
    progress_bar(30, 3, " > Initializing Systems")
    type_print(" > All systems online.")


def login_screen():
    clear_screen()
    header_login = "SCP FOUNDATION TERMINAL - LOGIN"
    type_print(header_login)
    pause()

def main():
    start_up()

if __name__ == "__main__":
    main()