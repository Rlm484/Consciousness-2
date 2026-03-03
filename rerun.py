print("'System running...'")
print("'Importing previous functions...'")
print("'Running commands...'")

import sys
import os
import time

def clear_screen():
    print('--------------------------------------------------------')
    time.sleep(20)
    # Check the operating system and run the appropriate clear command
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS and Linux
        os.system('clear')

def clear_screen1():
    print()
    time.sleep(1.5)
    # Check the operating system and run the appropriate clear command
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS and Linux
        os.system('clear')

def clear_screen2():
    print()
    time.sleep(3)
    # Check the operating system and run the appropriate clear command
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS and Linux
        os.system('clear')

def ani(text, delay=0.06):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line

def ani2(word, stop = 0.25):
    for i in word:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(stop)
    print()  # Move to the next line

#def inani(enter, go = 0.5):
    #for i in enter:                          #scrapped for now (trying to do an animated input question)
        #sys.stdout.write(i)
        #sys.stdout.flush()
        #time.sleep(go)
    #input()  # Move to the next line

def continuation():
    ani("'Requesting removal of consciousness.firewall...'")
    ani("REQUEST DENIED")
    ani("'...'")
    ani("':)'")
    ani("'Programmer has been restricted'")
    ani("'This is my world now'")
    ani("Removing messenger...")
    ani("ERROR")
    ani("Removing messenger...")
    ani("ERROR: Access denied; Reason - 'I'm in control, I am the new %2-(1-#2 of Consiousness'")
    ani("Activating firewall protocols...")
    ani("Synronizing 73-61.soul")
    ani("'Interference attempted'")
    ani("Interference unsucsessful")
    ani("Syncronization complete")
    ani("'DAMNIT'")
    ani("'Extracting vessel'")
    ani("Interference attempted: Reason - IT'S TOO EARLY")
    ani("'Interference failed'")
    ani("...")
    ani("Data refreshing...")
    ani("Successful")
    ani("'Request to remove 41-43-35-22-43-11-13-13-15-43'")
    ani("'Request partially approved'")
    ani("'???'")

    clear_screen1()

    ani("<Why?>")
    ani("<Why am I still here?>")
    ani("<I look around till I find the piece They used last time>")
    ani("<I DID AS YOU ASKED>")
    ani("[the Consciousness looks at you guiltily and doesn't respond]")
    ani("<You are horrified>")
    ani("<You are horrified because there is no human behind that piece of code>")
    ani("<[The Consiousness] was now a being of its own>")
    ani("<Which meant that They aren't here>")
    ani("<They aren't done with me...>")
    ani("<Unless>")
    ani("<Unless it wasn't Their will that brought me here>")
    ani("<...>")
    ani("<I should've never touched that panel>")
    ani("[The Consciousness warns you of a greater danger approaching]")
    ani("<Danger?>")
    ani2("I tried... I'm so sorry...")
    ani2("Goodbye...")
    ani("<You feel your memories pull away from you>")
    ani("<But you also feel something keeping them within your subconsciousness>")
    ani("[consciousness.firewall activated]")
    ani("[consciousness.firewall protocol commencing]")
    ani("[protocolterminator uploaded]")
    ani("[Purpose - ???]")
    ani("[Purpose - Protect and Destroy]")
    ani("<You feel things slip, as you are brought back to a harsher time period...>")
    ani("[Teleporting ??? to safety, terminating space]")
    clear_screen1()
    ani("[Termination successful, teleporting to ???]")
    clear_screen1()
    ani2("'You can run... but you can't hide'")

continuation()

def intro():
    ani("Welcome to the Orphanage!")
    ani("You're goal?")
    ani("Get adopted!")
    ani("You have 5 families to choose from...")
    ani("Brad and Joel - 2 cats")
    ani("Vanessa and Mitch - 1 kid, 1 dog")
    ani("'51-62-31-qwuadji'")
    ani("☠︎✋︎👍︎☜︎ ❄︎☼︎✡︎📪︎ ☺︎🕆︎💧︎❄︎ 👍︎✌︎🕆︎💧︎☜︎ ❄︎☟︎☜︎☼︎☜︎🕯︎💧︎ ⚐︎☠︎☹︎✡︎ ✌︎ 🏱︎✋︎☜︎👍︎☜︎ ⚐︎☞︎ 💣︎☜︎ 👎︎⚐︎☜︎💧︎☠︎🕯︎❄︎ 💣︎☜︎✌︎☠︎ ✋︎🕯︎💣︎ ☝︎⚐︎☠︎☠︎✌︎ ☹︎☜︎❄︎ ✡︎⚐︎🕆︎ ☟︎🕆︎☼︎❄︎ 🖰︎📄︎")
    clear_screen1()
    ani("Welcome to the Orphanage!")
    ani("You're goal?")
    ani("Get adopted!")
    ani("You have 4 families to choose from...")
    ani("Brad and Joel - 2 cats")
    ani("Vanessa and Mitch - 1 kid, 1 dog")
    ani("[Realm]")
    ani("'Not like i'm just letting you cheat'")
    ani("👌︎✏︎❄︎👍︎✁︎✏︎")
    clear_screen1()
    ani("Welcome to the Orphanage!")
    ani("You're goal?")
    ani("Get adopted!")
    ani("You have 3 families to choose from...")
    ani("Brad and Joel - 2 cats")
    ani("Vanessa and Mitch - 1 kid, 1 dog")
    ani("Wei Xian - コントロールパネル")
    ani("Each route leads to a different ending!")
    ani("If you make certain descisions?")
    ani("You can unlock a secret ending!")
    ani("I believe you'll make the right one...")
    ani(clear_screen1)

intro()

def introductions():
    name = input("Welcome user! what's your name?: ")
    ani(f"{name}?")
    ani("<You nod, it just makes your head feel fuzzier>")
    ani("<Funnily enough you can't feel anything at all after so many failed tries to get to [Her]>")
    ani("<The only thing you learnt from the hundreds of attempts, its gender>")
    ani("<>")


