from saveloader import detectSave, loadSystemSave
from rich import print as rprint
from clear import clear
from checkbadge import calculateBadge
from time import sleep
import sys
<<<<<<< HEAD
from mod import systemList, proList
from player import startGame, beginMenu, pauseBeginMenu

# compressed code helps make game much more expandable/moddable
=======
from player import beginMenu
from mod import *
>>>>>>> parent of bf87baf (code is a bit more finished, but still buggy)

# systems
sys.path.insert(0, './oses/')

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

    clear()
<<<<<<< HEAD
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
=======
    rprint('MiniChipOS ver. 0.59 - [bright_yellow]Codename Cookie Monster[/bright_yellow]')
    print('Ver. 12-30-2021\n\n')
    for i in range(len(pbList)):
        stri = pbList[i]
        stri1 = pbList[i - 1]
        save = loadSystemSave(stri)
        if save == False:
            rprint(f'[red]{i + 1}. {stri} - Get to level {pbProList[i - 1]} in {stri1} to unlock this![/red]')
        else:
            badge = calculateBadge(save, pbProList[i])
            print(f"{i + 1}. {stri}", badge)


>>>>>>> parent of bf87baf (code is a bit more finished, but still buggy)

    choice = input()
    startup(choice)

boot()