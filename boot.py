from saveloader import detectSave, loadSystemSave
from rich.console import Console
from time import sleep
import sys
from mod import systemList, proList, calculateBadge, clear
from player import startGame, beginMenu, pauseBeginMenu

# compressed code helps make game much more expandable/moddable

width = 120
console = Console(width=width)
style = "default on default"

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
    stri = systemList[int(system) - 1]
    level = loadSystemSave(stri)
    pro = proList[int(system) - 1]
    badge = calculateBadge(level, pro)
    if level == False:
        boot()
    launch(stri, level, badge, pro)
    
def boot():

    detectSave()

    global currentSystem

    clear()

    console.print('MiniChipOS ver. 0.59 - [bright_yellow]Codename Cookie Monster[/bright_yellow]', style=style)
    console.print('Ver. 12-30-2021\n\n', style=style)
    
    for i in range(len(systemList)):
        stri = systemList[i]
        stri1 = systemList[i - 1]
        save = loadSystemSave(stri)
        if save == False:
            console.print(f'[red]{i + 1}. {stri} - Get to level {proList[i - 1]} in {stri1} to unlock this![/red]', style=style)
        else:
            badge = calculateBadge(save, proList[i])
            console.print(f"[green]{i + 1}. {stri}[/green]", badge, style=style)

    choice = input()
    startup(choice)

boot()