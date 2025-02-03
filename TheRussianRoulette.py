import random
import pyfiglet
import os
from playsound import playsound
import threading
import time

RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
BOLD = "\033[1m"
RESET = "\033[0m"
GREEN = "\033[32m"
LIGHT_GREEN = "\033[92m"
BRIGHT_CYAN = "\033[96m"

Alive_message_color = GREEN
Game_Over_message_color = RED
Spinning_message_color = YELLOW
delay = 1

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


sound1 = os.path.join(BASE_DIR, "Soundtracks", "Pink Soldiers (Extended Version) - Squid Game OST.mp3")
sound2 = os.path.join(BASE_DIR, "Soundtracks", "Sonido de Disparo de Revolver 38 - Efecto de Sonido.mp3")



def play_sound():
    playsound(sound1)
def play_sound2():
    playsound(sound2)


sound_thread = threading.Thread(target=play_sound, daemon=True)
sound_thread2 = threading.Thread(target=play_sound2, daemon=True)
sound_thread.start()


def main():
    clear_screen()
    print(welcome_message())
    
    while True:
        
        a = input(f"{CYAN}How many bullets will be in the revolver?{RESET} {BOLD}{GREEN}(1-5){RESET} ")
        if Get_Level(a):
            break

        else:
            print(f"{RED}Enter a correct number of bullets{RESET}")

    pistol_charger = bullet_spaces(int(a))

    print(Spinning_message())
    random.shuffle(pistol_charger)

    i = 0
    while i < len(pistol_charger):
        decision = input(f"{CYAN}Choose an action{RESET} {BRIGHT_CYAN}[s]pin [p]ull {RESET} {BOLD}{i+1}/6{RESET} ").lower().strip()
        if decision == 's':
            random.shuffle(pistol_charger)
            print(Spinning_message())
            i = 0

        elif decision == 'p':
            if pistol_charger[i] == 1:
                sound_thread2.start()
                print(Game_Over_message())
                time.sleep(delay)
                break
            else:
                print(f"{Alive_message()}")
                print()
                i += 1

        else:
            print(f"{RED}Choose a correct decision{RESET}")







def Get_Level(n):
    try:
        n = int(n)
        if 1 <= n <= 5:
            return True
        else:
            return False
    except ValueError:
        return False

def bullet_spaces(s):
    spaces = [0] * 6
    for i in range(s):
        spaces[i] = 1
    return spaces

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome_message():
    ascii_banner = pyfiglet.figlet_format("Russian Roulette", font="slant")
    return f"{BRIGHT_CYAN}{ascii_banner}{RESET}"


def Alive_message():
    return f"{Alive_message_color}You're alive{RESET}"

def Game_Over_message():
    return f"{Game_Over_message_color}GAME OVER{RESET}\n"

def Spinning_message():
    return f"{Spinning_message_color}* Spinning chamber *{RESET}\n"




if __name__ == "__main__":
    main()