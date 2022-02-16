from rich import print as rprint
from clear import clear


pbList = ["PB-DOS Shell", "Progressbar 1", "Progressbar 2", "Progressbar 3.14", "Progressbar NOT 3.60", "Progressbar 95", "Progressbar 95 Plus", "Progressbar NOT 4.0", "Progressbar 98", "Progressbar 2000", "Progressbar Meme", "Progressbar XB", "Progressbar Wista", "Progressbar 7", "Progressbar 81", "Progressbar 10", "Progressbar 1X", "Progressbar 11"]
pbProList = [10, 10, 10, 10, 10, 10, 20, 30, 20, 30, 30, 30, 40, 40, 50, 50, 60, 60]

def addtionalFeatures(systemname):
    global diffLevel, pbList, pbProList
    # Built-in additional features:
    #   startEasyGame(): enables easy mode

    # example of how to add programs (exclude the for loop :P):
    for i in pbList:
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