from clear import clear
from rich.console import Console
from time import sleep
import random
import os
from saveloader import editSystemSave, addSystemSave
from checkbadge import calculateBadge
from mod import addtionalFeatures, bgColor, style
from mod import systemList as OSList
cancelPopUp = False
diffLevel = 1

width = 120
console = Console(width=120)

def wait():
    clear()
    console.print('P l e a s e  w a i t . . .\n\n\n', style=style)
    sleep(3)

# shutdown woohoo
def shutdown():
    wait()
    console.print('[bold orange]It is now safe to close your Command Line Interface.[/bold orange]', style=style)
    sleep(2)
    quit()

def restart():
    wait()
    from boot import boot
    boot()

# Begin menu normally
def beginMenu(systemname, systemlevel, systempro):
    os.system(bgColor)
    clear()
    if systemlevel > 1:
        console.print('╔════════════════════════╗\n║   B e g i n  M e n u   ║\n║    1 - Load Game       ║\n║    2 - New Game        ║\n║    3 - Restart         ║\n║    4 - Shutdown        ║\n╚════════════════════════╝\n', style=style)
    else:
        console.print('╔════════════════════════╗\n║   B e g i n  M e n u   ║\n║    1 - New Game        ║\n║    2 - Restart         ║\n║    3 - Shutdown        ║\n╚════════════════════════╝\n', style=style)
    choice = input()
    if choice == "1":
        if systemlevel > 1:
            addtionalFeatures(systemname)
            startGame(systemname, systemlevel, systempro)
        else:
            addtionalFeatures(systemname)
            editSystemSave(systemname, 1)
            startGame(systemname, 1, systempro)
    elif choice == "2":
        if systemlevel > 1:
            addtionalFeatures(systemname)
            editSystemSave(systemname, 1)
            startGame(systemname, 1, systempro)
        else:
            restart()
    elif choice == "3":
        if systemlevel > 1:
            restart()
        else:
            shutdown()
    elif choice == "4":
        shutdown()
    else:
        beginMenu(systemname, systemlevel, systempro)


# Begin menu during gameplay
def pauseBeginMenu(systemName, systemPro):
    clear()
    console.print('╔════════════════════════╗\n║   B e g i n  M e n u   ║\n║    1 - Resume          ║\n║    2 - New Game        ║\n║    3 - Restart         ║\n║    4 - Shutdown        ║\n╚════════════════════════╝\n', style=style)
    choice = input()
    if choice == "1":
        return
    elif choice == "2":
        editSystemSave(systemName, 1)
        startGame(systemName, 1, systemPro)
    elif choice == "3":
        restart()
    elif choice == "4":
        shutdown()
    else:
        pauseBeginMenu(systemName, systemPro)

# original code by Setapdede, but i refined it a bit.
def spawnPopup(startLevel, systemLabel):
    clear()
    os.system(bgColor)
    console.print('Level', startLevel)
    global cancelPopUp
    global popNum
    if systemLevel > 0:
        console.print('<', systemLabel, '>', style=style)
    if cancelPopUp == False:
        popNum = random.randint(0, 2)
    popText = ["Annoying Popup", " Can I help?  ", "  Hello!      "]
    popup = popText[popNum]
    console.print("[bold bright_black]╔════════════════════╗\n║[/bold bright_black] :) ", popup, "[bold bright_black]║\n║[/bold bright_black]        [OK]        [bold bright_black]║\n╚════════════════════╝[/bold bright_black]")
    popupinput = input()
    if popupinput.lower() == "ok":
        clear()
        os.system(bgColor)
    else:
        cancelPopUp = True
        spawnPopup(startLevel, systemLabel)

def startGame(systemName, startLevel, proLevel):
    global progressbar # total progressbar progress
    global progressbar2 # total orange segments in progressbar
    global lives
    global score
    global bar # array that contains segments for the progressbar
    global bar2 # contents in bar that are used to calculate pink segments
    global bardisplay # bar[] contents are displayed on screen
    global segments # used in conjunction with bardisplay
    global systemLabel # current system label
    global systemLevel # current system level (used with systemLabel)

    # setting global variables
    progressbar = 0
    progressbar2 = 0
    lives = 3
    score = 0
    bar = []
    bar2 = []
    bardisplay = ""
    segments = ""

    systemLabel = calculateBadge(startLevel, proLevel)

    if systemLabel == "What?":
        systemLevel = 6
    elif systemLabel == "Grand":
        systemLevel = 5
    elif systemLabel == "Adept":
        systemLevel = 4
    elif systemLabel == "Master":
        systemLevel = 3
    elif systemLabel == "Expert":
        systemLevel = 2
    elif systemLabel == "Pro":
        systemLevel = 1
    else:
        systemLevel = 0

    while True:
        # clears the screen for next segment
        clear()
        os.system(bgColor)
        global cancelPopUp
        # checks if lives are 0, breaks if true
                # checks if lives are 0, breaks if true
        if lives <= 0:
            console.print("[bold bright_blue]You are out of lives. Game over![/bold bright_blue]")
            if startLevel == 1:
                console.print('[i]A level has not been taken.[/i]', style=style)
            else:
                startLevel -= 1
                console.print('[bold i]-1 Level[/bold i]', style=style)
                editSystemSave(systemName, startLevel)
            lives = 3
            sleep(3)

            clear()
        popupshow = random.randint(0, 6)
        if popupshow == 6:
            cancelPopUp = False
            spawnPopup(startLevel, systemLabel)

        console.print('Level', startLevel)
        if systemLevel > 0:
            console.print('<', systemLabel, '>', style=style)

        # randomly chooses a segment and loads art
        segArt = ["[dark_blue]╔══╗\n║  ║\n║  ║\n╚══╝[/dark_blue]", "[bright_red]╔══╗\n║!!║\n║!!║\n╚══╝[/bright_red]", "[bright_magenta]╔══╗\n║--║\n║--║\n╚══╝[/bright_magenta]", "[bright_yellow]╔══╗\n║~~║\n║~~║\n╚══╝[/bright_yellow]", "[bright_black]╔══╗\n║..║\n║..║\n╚══╝[/bright_black]", "[bright_cyan]╔══╗\n║**║\n║**║\n╚══╝[/bright_cyan]"]
        if diffLevel == 0:
            segEasy = random.randint(0, 11)
            if segEasy <= 3:
                seg = 0
                console.print(segArt[seg])
            elif segEasy == 3:
                seg = 1
            elif segEasy == 4:
                seg = 2
            elif segEasy == 5 or segEasy == 6:
                seg = 3
            elif segEasy == 7 or segEasy == 8:
                seg = 4
            elif segEasy >= 9:
                seg = 5
            console.print(segArt[seg], style=style)
        if diffLevel == 1:
            seg = random.randint(0, 5)
            for i in range(6):
                if seg == i:
                    console.print(segArt[i], style=style)

        # green segment check
        greenseg = random.randint(0, 100)
        if greenseg == 95:
            seg = 6
            console.print("[bright_green]╔══╗\n║$$║\n║$$║\n╚══╝[/bright_green]", style=style)

        # checks if you have 1 life left
        if lives == 1:
            console.print("You have [italic bright_red]1 life left[/italic bright_red]. Be careful.", style=style)
        else:
            console.print("You have", lives, "lives left.", style=style)

        # checks if you have orange segments in your bar
        if progressbar2 > 0:
            console.print('\nYour bar:', end='', style=style)
            for segment in bar2:
                if segment == "Blue":
                    console.print("[blue][][/blue]", end='', style=style)
                elif segment == "Orange":
                    console.print("[bright_yellow][][/bright_yellow]", end='', style=style)
            console.print("\nYou have", progressbar, "% with", progressbar2, "% orange in your progressbar.", style=style)
        else:
            console.print('\nYour bar:', end='', style=style)
            for segment in bar2:
                if segment == "Blue":
                    console.print("[blue][][/blue]", end='', style=style)
            console.print("\nYou have", progressbar,"%", "in your progressbar.", style=style)

        # catches the currently displayed segment
        console.print("Type 'c' to catch, any other key to move away, and 'q' to quit.\n", style=style)
        catch = input()

        # calculates which segment you caught and does stuff
        if catch == "c":
            if seg == 0:
                progressbar += 5
                bar2.append("Blue")
                score += 5
            elif seg == 1:
                bar = []
                bar2 = []
                bardisplay = ""
                lives = lives - 1
                progressbar = 0
                progressbar2 = 0
                score -= 10
            elif seg == 2:
                if progressbar == 0:
                    continue
                if bar2[-1] == "Orange":
                    progressbar2 -= 5
                    progressbar -= 5
                    bar2.pop(-1)
                    score += 5
                else:
                    progressbar -= 5
                    bar2.pop(-1)
                    score += 5
            elif seg == 3:
                progressbar += 5
                progressbar2 += 5
                bar2.append("Orange")
            elif seg == 4:
                continue
            elif seg == 5:
                bonus = random.randint(0, 1)
                if bonus == 0:
                    progressbar += 10
                    for i in range(2):
                        bar2.append("Blue")
                    score += 10
                else:
                    progressbar += 15
                    for i in range(3):
                        bar2.append("Blue")
                    score += 15
            elif seg == 6:
                progressbar = 100
                progressbar2 = 0
                score += 100

        elif catch == "q":
            console.print('Game Over! Thanks for playing!', style=style)
            sleep(3)
            beginMenu(systemName, startLevel, proLevel)

        elif catch == "credits":
            clear()
            console.print('ProgressCLI95 0.2.2 Release', style=style)
            console.print('Original code (0.1) by Setapdede', style=style)
            console.print('Improved code (0.2-0.2.2) by BurningInfern0', style=style)
            console.print('Moddable code (0.3+) by CreateSource/AbnormalHare', style=style)
            console.print('Made for use with Sparrow Assistant by pivinx1', style=style)
            console.print('\nPress ENTER to get back to the game.', style=style)
            input()

        elif catch == "beginmenu":
            pauseBeginMenu(systemName, proLevel)

        # if you have 100% on your progressbar, the game will end.
        if progressbar >= 100:
            clear()
            os.system(bgColor)
            if progressbar2 > 0:
                console.print('Bravo!', style=style)
            elif progressbar >= 100 and progressbar2 == 0:
                console.print('Perfect!', style=style)
            elif progressbar > 100:
                console.print('Outer space!', style=style)
            if progressbar == 50 and progressbar2 == 50:
                console.print ('Yin and yang', style=style)
            if progressbar == 0 and progressbar2 == 100:
                console.print ("Nonconformist!", style=style)
            startLevel += 1
            editSystemSave(systemName, startLevel)
            if startLevel == proLevel:
                console.print('\nCongratulations! You are the Professional!', style=style)
                console.print('Pro Label acquired!', style=style)
                systemLevel = 1
                systemLabel = "Pro"
                console.print(f'{systemName} unlocked...', style=style)
                for i in range(len(OSList)):
                    if systemName == OSList[i]:
                        try:
                            addSystemSave(OSList[i + 1])
                        except:
                            addSystemSave(OSList[1])
            elif startLevel == 100:
                console.print('\nExpert Label acquired!', style=style)
                systemLevel = 2
                systemLabel = "Expert"
            elif startLevel == 250:
                console.print('\nMaster Label acquired!', style=style)
                systemLevel = 3
                systemLabel = "Master"
            elif startLevel == 500:
                console.print('\nAdept Label acquired!', style=style)
                systemLevel = 4
                systemLabel = "Adept"
            elif startLevel == 1000:
                console.print('\nGrand Label acquired!', style=style)
            elif startLevel == 2147483647:
                console.print('\nWhat?', style=style)
                systemLevel = 5
                systemLabel = "Grand"
            bar = []
            bar2 = []
            bardisplay = ""
            segments = ""
            progressbar = 0
            progressbar2 = 0
            console.print('\nPress ENTER to play another level.', style=style)
            input()
        continue

os.system("color 07")