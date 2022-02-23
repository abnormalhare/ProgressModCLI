from rich import print as rprint
from clear import clear

systemList = ["PB-DOS Shell", "Progressbar 1", "Progressbar 2", "Progressbar 3.14", "Progressbar NOT 3.60", "Progressbar 95", "Progressbar 95 Plus", "Progressbar NOT 4.0", "Progressbar 98", "Progressbar 2000", "Progressbar Meme", "Progressbar XB", "Progressbar Wista", "Progressbar 7", "Progressbar 81", "Progressbar 10", "Progressbar 1X", "Progressbar 11"]
proList = [10, 10, 10, 10, 10, 10, 20, 30, 20, 30, 30, 30, 40, 40, 50, 50, 60, 60]
bgColor = 'setterm -background blue -store'
style = "default on blue"

def addtionalFeatures(systemname):
    global diffLevel
    # Built-in additional features:
    #   startEasyGame(): enables easy mode
    # example of how to add programs (exclude the for loop :P):
    for i in systemList:
        if i == "Progressbar 95" or i == "Progressbar 95 Plus":
            continue
        if systemname == i:
            clear()
            rprint('╔════════════════════════╗\n║    G a m e m o d e     ║\n║    [green]1 - Easy[/green]            ║\n║    [blue]2 - Normal[/blue]          ║\n╚════════════════════════╝\n')
            choice = input()
            if choice == "1":
                diffLevel = 0
            elif choice != "2":
                addtionalFeatures()

def calculateBadge(level, proLevel):
    # i know you can probably use case statements here but i'm using if statements because it's easier. -Inferno
    if level >= 2147483647:
        return "What?"
    elif level >= 1000:
        return "Grand"
    elif level >= 500:
        return "Adept"
    elif level >= 250:
        return "Master"
    elif level >= 100:
        return "Expert"
    elif level >= proLevel:
        return "Pro"
    elif level < proLevel:
        return ""
    else:
        return "Calculation error."