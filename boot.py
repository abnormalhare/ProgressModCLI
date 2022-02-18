from saveloader import detectSave, loadSystemSave
from rich import print as rprint
from rich.console import Console
from clear import clear
from checkbadge import calculateBadge
from time import sleep
import sys
from player import beginMenu
from mod import *
import re

width = 120
console = Console(width=width)
message = ""

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
    global width
    global message

    clear()

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



    choice = input()
    startup(choice)

comp()