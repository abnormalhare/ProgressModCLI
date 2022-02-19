from saveloader import detectSave, loadSystemSave
from rich import print as rprint
from rich.console import Console
from clear import clear
from checkbadge import calculateBadge
from time import sleep
import sys
<<<<<<< HEAD
<<<<<<< HEAD
from player import beginMenu
from mod import *
import re

width = 120
console = Console(width=width)
message = ""
=======
=======
>>>>>>> parent of 33673a8 (UNFINISHED SAVE)
from mod import systemList, proList
from player import startGame, beginMenu, pauseBeginMenu

# compressed code helps make game much more expandable/moddable
<<<<<<< HEAD
>>>>>>> parent of 33673a8 (UNFINISHED SAVE)
=======
>>>>>>> parent of 33673a8 (UNFINISHED SAVE)

# systems
sys.path.insert(0, './oses/')

def fillBg():
    global message
    message2 = message
    message3 = ""
    x = 0
    for i in message:
        if i == "[":
            x += 1
        elif i == "]" and x:
            x -= 1
        elif x == 0:
            message3 += i
    message2 += " " * (width - len(message3))
    message = message2

def launch(systemOS, systemlevel, systembadge, systempro):
    clear()
    print(" ".join(systemOS))
    print(systembadge)
    print('\n\n\nNow Loading...')
    sleep(4)
    beginMenu(systemOS, systemlevel, systempro)

def startup(system):
    # string from mod.py
    stri = systemList[int(system) - 1]
    # originally "level95", "check95plus", etc
    level = loadSystemSave(stri)
    # removes "necessity" for each os to have a separate pro variable, mod.py
    pro = proList[int(system) - 1]
    # originally "badge95", etc
    badge = calculateBadge(level, pro)
    if level == False:
        boot()
    launch(stri, level, badge, pro)
    
def boot():

    detectSave()

    global currentSystem
    global width
    global message

    clear()
<<<<<<< HEAD
<<<<<<< HEAD

    message = 'MiniChipOS ver. 0.59 - [bright_yellow]Codename Cookie Monster[/bright_yellow]'
    style = "default on dark_blue"
    fillBg()
    console.print(message, style=style)
    for i in range(len(pbList)):
        stri = pbList[i]
        stri1 = pbList[i - 1]
        save = loadSystemSave(stri)
        if save == False:
            message = f'[red]{i + 1}. {stri} - Get to level {pbProList[i - 1]} in {stri1} to unlock this![/red]'
            fillBg()
            console.print(message, style=style)
        else:
            badge = calculateBadge(save, pbProList[i])
            message = f"[#00bb00]{i + 1}. {stri} {badge}[/#00bb00]"
            fillBg()
            console.print(message, style=style)
=======
    rprint('MiniChipOS ver. 0.56 - [bright_yellow]Codename Nubo[/bright_yellow]')
    print('Ver. 12-30-2021\n\n')
    
    for i in range(len(systemList)):
        stri = systemList[i]
        stri1 = systemList[i - 1]
        save = loadSystemSave(stri)
        if save == False:
            rprint(f'[red]{i + 1}. {stri} - Get to level {proList[i - 1]} in {stri1} to unlock this![/red]')
        else:
            badge = calculateBadge(save, proList[i])
            print(f"{i + 1}. {stri}", badge)
>>>>>>> parent of 33673a8 (UNFINISHED SAVE)
=======
    rprint('MiniChipOS ver. 0.56 - [bright_yellow]Codename Nubo[/bright_yellow]')
    print('Ver. 12-30-2021\n\n')
    
    for i in range(len(systemList)):
        stri = systemList[i]
        stri1 = systemList[i - 1]
        save = loadSystemSave(stri)
        if save == False:
            rprint(f'[red]{i + 1}. {stri} - Get to level {proList[i - 1]} in {stri1} to unlock this![/red]')
        else:
            badge = calculateBadge(save, proList[i])
            print(f"{i + 1}. {stri}", badge)
>>>>>>> parent of 33673a8 (UNFINISHED SAVE)

    choice = input()
    startup(choice)

boot()