from saveloader import detectSave, loadSystemSave
from rich import print as rprint
from clear import clear
from checkbadge import calculateBadge
from time import sleep
import sys
from player import beginMenu
from mod import *

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
    stri = pbList[int(system) - 1]
    level = loadSystemSave(stri)
    pro = pbProList[int(system) - 1]
    badge = calculateBadge(level, pro)
    if level == False:
        boot()
    launch(stri, level, badge, pro)

def comp():
    detectSave()
    clear()
    rprint('MiniChipOS ver. 0.59 - [bright_yellow]Codename Cookie Monster[/bright_yellow]')
    print('Ver. 12-30-2021\n\n')
    rprint("[blue]Choose your system.[/blue]")
    if loadSystemSave("BarOS 1"):
        rprint("[green]1.Progress Computer\n2. Progresh[/green]")
    else:
        rprint("[green]1. Progress Computer[/green]\n[red]2. Progresh[/red]")
    choice = input()
    boot(choice)

def boot(choice):

    detectSave()

    global currentSystem

    clear()
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



    choice = input()
    startup(choice)

comp()