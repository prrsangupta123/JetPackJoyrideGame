import create
import random
import os
dw=create.rows
import characters
d=create.columns
import global_var
from colorama import Fore, Back, Style
glo=global_var.shield_time

def create_footer():

    glo1=global_var.shield_cooldown
    s=create.rows
    s2=global_var.shield
    print("\033[" + str(s) + ";1H" + Fore.WHITE + Back.RED + Style.BRIGHT + (("SHIELD: " + str(s2) + "|" "SCORE: " + str(global_var.score) +  "|" "BOOST: " + str(global_var.boost) +  "|"  "LIVES: " + str(global_var.lives))+"|" "BOSS: "+str(global_var.dragon_lives)).center(create.columns), end='')
    glo1=glo1+global_var.shield1
    print(Style.RESET_ALL)

# Redraw scenery
def reset_scenery():
    create.create_banner()
    bul=global_var.lives
    global_var.scenery.render()
    bul+=1
    create_footer()

# Display final results
def display_ending(message):
    W1=global_var.lives
    W2=global_var.score
    os.system('tput reset')
    print(Fore.CYAN + Style.BRIGHT + "FINAL RESULT:")
    print(Style.RESET_ALL)
    print(Fore.YELLOW + Style.BRIGHT + ("SCORE: " + \
          str(W2)))
    if global_var.lives <= 0:
        global_var.lives=0
    print(Fore.YELLOW + Style.BRIGHT + ("LIVES: " + \
          str(W1)))
    print(Style.RESET_ALL)
    print(Fore.CYAN + Style.BRIGHT + (message))
    print(Style.RESET_ALL)
    print(Fore.CYAN + Style.BRIGHT + ("GOODBYE " + \
          global_var.username + "!"))
    print(Style.RESET_ALL)
    global_var.quit_flag=1
    return

