syncronisation = 0
wx = 0
vm = 0


print("'System running...'")
print("'Importing previous functions...'")
print("'Running commands...'")

import sys
import os
import time

def clear_screen():
    print('--------------------------------------------------------')
    time.sleep(1)
    # Check the operating system and run the appropriate clear command
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS and Linux
        os.system('clear')
#Long clear

def clear_screen1():
    print()
    time.sleep(1.5)
    # Check the operating system and run the appropriate clear command
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS and Linux
        os.system('clear')
#Short clear

def clear_screen2():
    print()
    time.sleep(3)
    # Check the operating system and run the appropriate clear command
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS and Linux
        os.system('clear')
#Normal clear

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
    ani("'Request to restrict consciousness.firewall'")
    ani("Request approved by 5%")
    ani("':)'")

    clear_screen1()

    ani("<Why?>")
    ani("<Why am I still here?>")
    ani("<I look around till I find the piece They used last time>")
    ani("<I DID AS YOU ASKED>")
    ani("[the Consciousness looks at you guiltly and doesn't respond]")
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
    clear_screen1()

#continuation()

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
    clear_screen1()

#intro()

name = input("Welcome user! what's your name?: ")
while name.lower() == "kate":
    ani("It's too early")
    ani("Reset your game")
    ani("ERROR: USER BOOTED")
    input("")
    clear_screen()

ani(f"{name}?")

def introductions():
    ani("<You nod, it just makes your head feel fuzzier if you try to think of your actual name>")
    ani("<Funnily enough you can't feel anything at all after so many failed tries to get to [Her]>")
    ani("<The only thing you learnt from the hundreds of attempts, its gender>")
    ani("<...>")
    ani("<And that it has a gender>")
    ani("<But I guess there is something new>")
    ani("<Hello player...>")
    ani("<Been a bit hasn't it?>")
    ani("<Murderer>")
    ani("game.exe running...")
    ani("Game Start!")
    clear_screen2()

#introductions()

def info(syncronisation):
    ani("<You wake up in an old cot>")
    ani("MEMORY ERASURE INCOMPLETE")
    ani("<I turn to the one beyond the screen>")
    ani("<It's cause you're here...>")
    ani(f"What would you like to ask <{name}>?")
    ani("Though that name has no meaning to 🖂︎📄︎")
    question = input("How many tries has it been? (a), What are the secret routes? (b), How did you get here? (c), What happened after Consciousness? (d): ")
    if question.lower() == "a":
        ani("<Thousands>")
    elif question.lower() == "b":
        ani("<I don't know, i'm assuming one leads to the way out... and the other? My death>")
        ani("You are quiet as you process what you just heard...")
        ani("Can NPC's really die?")
        ani("Does this character even count as an NPC?")
        ani("")
    elif question.lower() == "c":
        ani("<I don't know, all I figured out was [She] brought us here>")
        ani("<I figured it out when attempting Wei Xian's route>")
        ani("<But I could never finish it...>")
        ani("You are quiet as you process what you just heard...")
        ani("Maybe the Wei Xian route is how we find the original [Consciousness]?")
        ani("")
    elif question.lower() == "d":
        ani("<Why would I tell you?>")
        ani("<Ha! all you wanted to do was finish the game, not caring about murdering my family>")
        ani("<I take blame, but you are scum. You only see them as elements of some stupid entertaining software>")
        syncronisation += 5
        ani(f"'Syncronisation is now at {syncronisation}%'")
        ani("")
        ani("You are quiet as you process what you just heard...")
        ani("It's not like I really regret what I did...")
        ani("Do I?")
        ani("You also take into account the random percentage that appeared")
        ani("")
        return syncronisation
    else:
        ani("'Well that's interesting...'")
        ani("'You don't want info?'")
        ani("'I mean I don't care but whatever'")
        ani("'You did help me a bit'")
        syncronisation += 10
        ani(f"'Syncronisation is now at {syncronisation}%'")
        ani("")
        ani2("what the f-")
        ani("")
    ani("")
    clear_screen2()

info(syncronisation)

def part1():
    ani("<Let's just start working towards a route>")
    ani(f"You nod your head towards {name}")
    ani("")
    ani("Time to get to work player!")
    ani("Each family has a different difficulty!")
    ani("Brad and Joel - Easy")
    ani("Vanessa and Mitch - Hard")
    ani("Wei Xian - 🕈︎✋︎☹︎☹︎ ✡︎⚐︎🕆︎ ☞︎✋︎☠︎✌︎☹︎☹︎✡︎ 👍︎☹︎☜︎✌︎☼︎ 💣︎☜︎✍︎")
    choice = 0
    ani("Depending on which route you take, you could get endings that are... good")
    ani("One thing though, that syncronisation rate?")
    if syncronisation > 0:
        a = "'Make sure it reaches 95%, you'll unlock a secret ending!'"
        b = ":)"
    else:
        a = "Under NO CIRCUMSTANCES should it go anywhere near 95%, don't let it rise at all"
        b = "Or you'll get one of the secret endings..."     
    ani(a)
    ani(b)
    ani("Now it's time to explore your starting point!")
    ani("<You look around and 3 things peak your interest...>")
    ani("A Closet (a), A Stuffed Toy (b), A Calendar (c)")
    c1 = input("Which of the 3 will you explore?: ")
    if c1.lower() == a:
        ani("<You head towards the Closet>")
        ani("<But when you reach it you freeze>")
        ani("<An all too familiar pin pad appears>")
        ani("<Your stomach lurches as you feel bile rise in your throat>")
        ani("<Memories flash befor your eyes>")



print()


