# SCP-10839 - "The Digital Oracle" is a terminal located in an impossible site that never existed. It holds knowledge on all current SCP's in existed
import time, string
import random
import os
import sys


# Helper Functions
def type_print(text, delay=0.015):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay + random.uniform(0, 0.02))
    print()

def pause(a=0.2, b=0.6):
    time.sleep(random.uniform(a, b))

def overwrite_line(text):
    sys.stdout.write("\r" + text)
    sys.stdout.flush()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def spinner(duration=3, message=" > Loading"):
    symbols = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    i = 0

    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(0.5)

    while time.time() < end_time:
        sys.stdout.write(f"\r{message}... {symbols[i % len(symbols)]}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write("\r" + " " * (len(message) + 10) + "\r")
    sys.stdout.flush()

def typed_progress_bar_single_line(total=20, duration=5, message=" > Processing"):
    
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(0.5)
    for i in range(total + 1):
        percent = int((i / total) * 100)
        bar = '#' * i + '-' * (total - i)

        sys.stdout.write(f"\r{message} [{bar}] {percent}%")
        sys.stdout.flush()
        time.sleep(duration / total)
    print()  # Move to the next line after progress bar finishes

def glitch_bar(length=12, intensity=0.5):
    
    glitch_chars = "#$%&█@!?"
    
    return ''.join(
        random.choice(glitch_chars) if random.random() < intensity else '█' 
        for _ in range(length)
                   )

def build_login_block(intensity=0.5):
    
    user_bar = glitch_bar(8, intensity)
    pass_bar = glitch_bar(8, intensity)

    line1 = f" > Username: [{user_bar}]"
    line2 = f" > Password: [{pass_bar}]"

    return line1 + "\n" + line2

def glitch_block(duration=5):

    start = time.time()

    while time.time() - start < duration:
        progress = (time.time() - start) / duration
        intensity = 0.1 + progress * 0.5  # Increase intensity over time

        sys.stdout.write("\033[2A")

        block = build_login_block(intensity)

        sys.stdout.write(block + "\n")
        sys.stdout.flush()
        time.sleep(0.08)

def corrupted_loading(message = " > Corrupted Data Detected..."):
    type_print(message, delay=0.05)
    type_print(" > Attempting to recover...", delay=0.05)
    spinner(5, " > Recovering")
    for _ in range(15):
        glitch_symbols = ['#', '-', ' ', '@', '%', '&']
        bar = ''.join(random.choice(glitch_symbols) for _ in range(20))
        overwrite_line(f" > [{bar}]")
        time.sleep(0.4)
    print()  # Move to the next line after glitch effect
    
def print_ascii_logo(mode):
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
    if mode == "fast":
        print(header)
        print("-" * 88)
        pause(1, 1.5)
    else:
        for line in header.splitlines():
            print(line)
            time.sleep(0.15)
        print("-" * 88)
        pause(1, 1.5)

def fast_fetch():
    # Simulate what fastfetch does in a linux terminal by displaying system information
    type_print(" > Fetching system information...")
    time.sleep(1)
    system_info = { 
        "OS": "O.R.A.C.L.E.",
        "Kernel": "Pataphysical Layer 5",
        "Uptime": f"{random.randint(1, 10)} days, {random.randint(0, 23)} hours, {random.randint(0, 59)} minutes, {random.randint(0, 59)} seconds",
        "CPU": "Singularity Core iX-Ω @ 3.7GHz",
        "RAM": "Akashic Cache Layer",
        "Storage": "Temporal Loop Storage Device",
        "Network": "Quantum Entanglement Interface (QEI) - 1Tbps"
    }
    for key, value in system_info.items():
        type_print(f" > {key}: {value}", delay=0.01)
        time.sleep(0.5)

# Boot Animation Functions
def start_up():
    print_ascii_logo("line")
    pause(0.5, 1.0)
    spinner(5, " > Powering on")
    pause(0.5, 1)
    boot_sequence()
    pause(0.5, 1)
    typed_progress_bar_single_line(30, 3, " > Initializing Systems")
    pause(0.5, 1)
    type_print(" > All systems online.")


def boot_sequence():
    greek_names = [
    "alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta",
    "iota", "kappa", "lambda", "mu", "nu", "xi", "omicron", "pi",
    "rho", "sigma", "tau", "upsilon", "phi", "chi", "psi", "omega"
                ]
    alpha = list(string.ascii_uppercase)

    # Simulate a boot sequence with various system checks
    spinner(4, " > Initializing Boot Sequence")
    pause(0.5, 1)
    spinner(8, " > Scanning for stable reality baseline")
    pause(0.5, 1)
    type_print(" > Stable Reality Found")
    pause(0.5, 1)
    spinner(6, " > Locating kernel access point")
    pause(0.5, 1)
    type_print(f" > Access point located in reality {random.choice(greek_names).title()} {random.choice(alpha)}{random.randint(14,987)}")
    pause(0.5, 1)
    typed_progress_bar_single_line(15, 4, " > Synchronizing Kernal Probability Shift")
    pause(0.5, 1)
    typed_progress_bar_single_line(25, 4, " > Loading Omniscient Research And Containment Logistics Environment (O.R.A.C.L.E.)")
    pause(0.5, 1)
    type_print(" > Checking hardware components...")
    fast_fetch()
    typed_progress_bar_single_line(20, 4, " > Running diagnostics")
    pause(0.5, 1)
    type_print(" > Hardware check complete. No issues found.")
    pause(0.5, 1)
    type_print(" > Loading user interface...")
    pause(0.5, 1)
    spinner(4, " > Starting terminal services")
    pause(0.5, 1)
    type_print(" > Terminal ready.")
    pause(0.5, 1)

def login_screen():
    clear_screen()
    print_ascii_logo("fast")
    type_print(" > SCP FOUNDATION TERMINAL - LOGIN", delay=0.05)
    pause()
    
    print("> Username: [████████]")
    print("> Password: [████████]")

    glitch_block(2)
    
    corrupted_loading(" > Access Denied. Corrupted credentials detected...")

def remote_access_override():
    type_print(" > Attempting to override remote access protocols...")
    pause(0.5, 1)
    spinner(5, " > Bypassing security measures")
    pause(0.5, 1)
    type_print(" > Override successful. Remote access granted.")
    pause(0.5, 1)
    type_print(" > Welcome to the O.R.A.C.L.E. Terminal O5-███.")
    pause(0.5, 1)

def main_menu():
        print_ascii_logo("fast")
        type_print(" > 1) SCP Files")
        pause(0.5, 1.0)
        type_print(" > 2) MTF Teams")
        pause(0.5, 1.0)
        type_print(" > 3) Foundation Sites")
        pause(0.5, 1.0)
        type_print(" > 4) Departments")
        pause(0.5, 1.0)

def scp_files(): 
    type_print(" > 1) List")
    pause(0.5, 1.0)
    type_print(" > 2) Search")
    pause(0.5, 1.0)
    input(" > Press enter to continue")

def mtf_teams():
    type_print(" > 1) List")
    pause(0.5, 1.0)
    type_print(" > 2) Search")
    pause(0.5, 1.0)
    type_print(" > 3) Current Missions")
    pause(0.5, 1.0)
    type_print(" > 4) Deploy")
    pause(0.5, 1.0)
    input(" > Press enter to continue")

def foundation_sites():
    type_print(" > 1) List")
    pause(0.5, 1.0)
    type_print(" > 2) Search")
    pause(0.5, 1.0)
    input(" > Press enter to continue")

def departments():
    type_print(" > 1) List")
    pause(0.5, 1.0)
    type_print(" > 2) Search")
    pause(0.5, 1.0)
    input("Press enter to continue")

def main_menu_chooser(choice):
    if choice == 1:
      scp_files()
    elif choice == 2:
        mtf_teams()
    elif choice == 3:
        foundation_sites()
    elif choice == 4:
        departments()
    else:
        type_print(" > Shutting down O.R.A.C.L.E Terminal. Goodbye, O5-███")
        pause(1, 1.5)
        

def main():
    start_up()
    login_screen()
    remote_access_override()
    main_menu()
    user_choice = int(input(" > "))
    main_menu_chooser(user_choice)

if __name__ == "__main__":
    main()
