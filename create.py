import shutil
import os
import sys
import termios
import tty
import time
from colorama import init, Fore, Back, Style

columns = 120
rows = 35
row2=40

def create_banner():
    matrix=row2+columns
    print("\033[2;1H" + Fore.WHITE + Back.RED + Style.BRIGHT +
          "WELCOME TO MANDALORIAN GAME".center(columns), end='')
    matrix+=1
    #print(Style.RESET_ALL)
    print(Back.BLUE)
    print(Style.RESET_ALL)

mag = [["*"],["*"]]

magnet = [["*", "*", "*"],
          ["*", " ", "*"],
          ["*", " ", "*"]]

columns2=columns*10

platform = [["W", "E", "L", "C", "O", "M", "E", " ", " ", " "],
            [" ", " ", " ", "T", "O", " ", " ", " ", " ", " "],
            ["M", "A", "N", "D", "A", "L", "O", "R", "I", "A"],
            ["N", " ", "G", "A", "M", "E", " ", " ", " ", " "]]

col, row = shutil.get_terminal_size()

INVALID = -1
s=time.time()

beamd = [['=', ' ', ' '], [' ', '=', ' '], [' ', ' ', '=']]

co,ro = os.get_terminal_size(0)
mando = [[" ", "@", " "],
         ["/", "|", "\\"],
         [" ", "|", " "],
         ["/", " ", "\\"]]

coin = [["$", "$", "$"]]

beamh = [["=", "=", "=", "=", "="]]

boostup = [["+"]]

bullet = [["=", ">"]]

bullet1 = [["(","-","-","-"]]

beamv = [["="], ["="], ["="], ["="], ["="]]

shield = [["S"]]


dragon = [
    list("                        _ "),   
    list(" __--/)  ._~~~>>>>>>   ' '"),    
    list("(._\  \ (   ~~>>>>>>.~._' "),   
    list("  -~}   \_~-  )~~>>>>' /  "),  
    list("    {     ~/   ~~~~~.-.-~ "),  
    list("     ~.(   '--~~/  /~~.   "), 
    list(" -~~~~ \  \__~( -.-~~- \  "), 
    list("'`-'~~-/  /   ~-..\ .__~/ "), 
    list("     ((_.`   ((__. ```_'  ")
    ]
mando1 = [[" ", "o", " "],
         ["/", "█", "\\"],
         [" ", "█", " "],
         ["/", " ", "\\"]]
# key presses
UP, LEFT, RIGHT, QUIT, FIRE, DOWN, SHIELD = range(7)
INVALID = -1
INVALID1=INVALID
# allowed inputs
_allowed_inputs = {
    UP: ['w', '\x1b[A'],
    LEFT: ['a', '\x1b[D'],
    RIGHT: ['d', '\x1b[C'],
    QUIT: ['q'],
    SHIELD: [' '],
    DOWN: ['s'],
    FIRE: ['f']
}

def get_key(key):
    for x in _allowed_inputs:
        INVALID1=INVALID-1
        if key in _allowed_inputs[x]:
            return x
    return INVALID

def printss(self):
    print(Fore.RED + "checking allowed inputs")

class _Getch:

    def __init__(self):
        self.impl = _GetchUnix()

    def __call__(self):
        return self.impl()

def prints(self):
    print(Fore.RED + "Input taking")

class _GetchUnix:

    def __init__(self):
        import tty
        import sys

    def __call__(self):
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        ks=1
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(ks)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

_getch = _Getch()

def printd(self):
    print(Fore.RED + "Game Over")

class AlarmException(Exception):
    pass

def alarmHandler(signum, frame):
    raise AlarmException
def printl(self):
    print(Fore.RED + "Input checking")
def get_input(timeout=1):
    import signal
    signal.signal(signal.SIGALRM, alarmHandler)
    # signal.alarm(timeout)
    w=0.5
    signal.setitimer(signal.ITIMER_REAL,w,w)
    qw=0
    try:
        text = _getch()
        signal.alarm(qw)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''
