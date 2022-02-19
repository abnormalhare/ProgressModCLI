from clear import clear
from rich import print as rprint
from time import sleep
import random
from saveloader import editSystemSave, addSystemSave
from checkbadge import calculateBadge
from mod import addtionalFeatures
from mod import systemList as OSList
cancelPopUp = False
diffLevel = 1


def wait():
    clear()
    print('P l e a s e  w a i t . . .\n\n\n')
    sleep(3)

# shutdown woohoo
def shutdown():
    wait()
    rprint('[bold orange]It is now safe to close your Command Line Interface.[/bold orange]')
    sleep(2)
    quit()

def restart():
    wait()
    from boot import boot
    boot()

# Begin menu normally
def beginMenu(systemname, systemlevel, systempro):
    clear()
    if systemlevel > 1:
        print('╔════════════════════════╗\n║   B e g i n  M e n u   ║\n║    1 - Load Game       ║\n║    2 - New Game        ║\n║    3 - Restart         ║\n║    4 - Shutdown        ║\n╚════════════════════════╝\n')
    else:
        print('╔════════════════════════╗\n║   B e g i n  M e n u   ║\n║    1 - New Game        ║\n║    2 - Restart         ║\n║    3 - Shutdown        ║\n╚════════════════════════╝\n')
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
    print('╔════════════════════════╗\n║   B e g i n  M e n u   ║\n║    1 - Resume          ║\n║    2 - New Game        ║\n║    3 - Restart         ║\n║    4 - Shutdown        ║\n╚════════════════════════╝\n')
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
    print('Level', startLevel)
    global cancelPopUp
    global popNum
    if systemLevel > 0:
        print('<', systemLabel, '>')
    if cancelPopUp == False:
        popNum = random.randint(0, 2)
    popText = ["Annoying Popup", " Can I help?  ", "  Hello!      "]
    popup = popText[popNum]
    rprint("[bold bright_black]╔════════════════════╗\n║[/bold bright_black] :) ", popup, "[bold bright_black]║\n║[/bold bright_black]        [OK]        [bold bright_black]║\n╚════════════════════╝[/bold bright_black]")
    popupinput = input()
    if popupinput.lower() == "ok":
        clear()
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
        global cancelPopUp
        # checks if lives are 0, breaks if true
                # checks if lives are 0, breaks if true
        if lives <= 0:
            rprint("[bold bright_blue]You are out of lives. Game over![/bold bright_blue]")
            if startLevel == 1:
                rprint('[i]A level has not been taken.[/i]')
            else:
                startLevel -= 1
                rprint('[bold i]-1 Level[/bold i]')
                editSystemSave(systemName, startLevel)
            lives = 3
            sleep(3)

            clear()
        popupshow = random.randint(0, 6)
        if popupshow == 6:
            cancelPopUp = False
            spawnPopup(startLevel, systemLabel)

        print('Level', startLevel)
        if systemLevel > 0:
            print('<', systemLabel, '>')

        # randomly chooses a segment and loads art
        segArt = ["[blue]╔══╗\n║  ║\n║  ║\n╚══╝[/blue]", "[bright_red]╔══╗\n║!!║\n║!!║\n╚══╝[/bright_red]", "[bright_magenta]╔══╗\n║--║\n║--║\n╚══╝[/bright_magenta]", "[bright_yellow]╔══╗\n║~~║\n║~~║\n╚══╝[/bright_yellow]", "[bright_black]╔══╗\n║..║\n║..║\n╚══╝[/bright_black]", "[bright_cyan]╔══╗\n║**║\n║**║\n╚══╝[/bright_cyan]"]
        if diffLevel == 0:
            segEasy = random.randint(0, 11)
            if segEasy <= 3:
                seg = 0
                rprint(segArt[seg])
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
            rprint(segArt[seg])
        if diffLevel == 1:
            seg = random.randint(0, 5)
            for i in range(6):
                if seg == i:
                    rprint(segArt[i])

        # green segment check
        greenseg = random.randint(0, 100)
        if greenseg == 95:
            seg = 6
            rprint("[bright_green]╔══╗\n║$$║\n║$$║\n╚══╝[/bright_green]")

        # checks if you have 1 life left
        if lives == 1:
            rprint("You have [italic bright_red]1 life left[/italic bright_red]. Be careful.")
        else:
            print("You have", lives, "lives left.")

        # checks if you have orange segments in your bar
        if progressbar2 > 0:
            print('\nYour bar:', end='')
            for segment in bar2:
                if segment == "Blue":
                    rprint("[blue][][/blue]", end='')
                elif segment == "Orange":
                    rprint("[bright_yellow][][/bright_yellow]", end='')
            print("\nYou have", progressbar, "% with", progressbar2, "% orange in your progressbar.")
        else:
            print('\nYour bar:', end='')
            for segment in bar2:
                if segment == "Blue":
                    rprint("[blue][][/blue]", end='')
            print("\nYou have", progressbar,"%", "in your progressbar.")

        # catches the currently displayed segment
        catch = input("Type 'c' to catch, any other key to move away, and 'q' to quit.\n")

        # calculates which segment you caught and does stuff
        if seg == 0 and catch == "c":
            progressbar = progressbar + 5
            bar2.append("Blue")
            score = score + 5
        elif seg == 1 and catch == "c":
            bar = []
            bar2 = []
            bardisplay = ""
            lives = lives - 1
            progressbar = 0
            progressbar2 = 0
            score = score - 10
        elif seg == 2 and catch == "c":
            if progressbar == 0:
                continue
            if bar2[-1] == "Orange":
                progressbar2 = progressbar2 - 5
                progressbar = progressbar - 5
                bar2.pop(-1)
                score = score + 5
            else:
                progressbar = progressbar - 5
                bar2.pop(-1)
                score + score - 5
        elif seg == 3 and catch == "c":
            progressbar = progressbar + 5
            progressbar2 = progressbar2 + 5
            bar2.append("Orange")
        elif seg == 4 and catch == "c":
            continue
        elif seg == 5 and catch == "c":
            bonus = random.randint(0, 1)
            if bonus == 0:
                progressbar = progressbar + 10
                bar2.append("Blue")
                bar2.append("Blue")
                score = score + 10
            else:
                progressbar = progressbar + 15
                bar2.append("Blue")
                bar2.append("Blue")
                bar2.append("Blue")
                score = score + 15
        elif seg == 6 and catch == "c":
            progressbar = 100
            progressbar2 = 0
            score = score + 100

        if catch == "q":
            print('Game Over! Thanks for playing!')
            sleep(3)
            beginMenu(systemName, startLevel, proLevel)

        if catch == "credits":
            clear()
            print('ProgressCLI95 0.2.2 Release')
            print('Original code (0.1) by Setapdede')
            print('Improved code (0.2-0.2.2) by BurningInfern0')
            print('Moddable code (0.3+) by CreateSource/AbnormalHare')
            print('Made for use with Sparrow Assistant by pivinx1')
            print('\nPress ENTER to get back to the game.')
            input()

        if catch == "beginmenu":
            pauseBeginMenu(systemName, proLevel)

        # if you have 100% on your progressbar, the game will end.
        if progressbar >= 100:
            if progressbar2 > 0:
                print('Bravo!')
            elif progressbar >= 100 and progressbar2 == 0:
                print('Perfect!')
            elif progressbar > 100:
                print('Outer space!')
            if progressbar == 50 and progressbar2 == 50:
                print ('Yin and yang')
            if progressbar == 0 and progressbar2 == 100:
                print ("Nonconformist!")
            startLevel += 1
            editSystemSave(systemName, startLevel)
            if startLevel == proLevel:
                print('\nCongratulations! You are the Professional!')
                print('Pro Label acquired!')
                systemLevel = 1
                systemLabel = "Pro"
                print(f'{systemName} unlocked...')
                for i in range(len(OSList)):
                    if systemName == OSList[i]:
                        try:
                            addSystemSave(OSList[i + 1])
                        except:
                            addSystemSave(OSList[1])
            elif startLevel == 100:
                print('\nExpert Label acquired!')
                systemLevel = 2
                systemLabel = "Expert"
            elif startLevel == 250:
                print('\nMaster Label acquired!')
                systemLevel = 3
                systemLabel = "Master"
            elif startLevel == 500:
                print('\nAdept Label acquired!')
                systemLevel = 4
                systemLabel = "Adept"
            elif startLevel == 1000:
                print('\nGrand Label acquired!')
            elif startLevel == 2147483647:
                print('\nWhat?')
                systemLevel = 5
                systemLabel = "Grand"
            bar = []
            bar2 = []
            bardisplay = ""
            segments = ""
            progressbar = 0
            progressbar2 = 0
            print('\nPress ENTER to play another level.')
            input()
        continue
