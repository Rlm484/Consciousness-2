#All of the following is non-canon, it is just to show me testing my code and debugging

#Got help from a friend
#name = 0

#def sync(name):
#    while name < 95:
#        try:
#            add = int(input("What is the added syncronisation rate? "))
#            name += add
#        except ValueError:
#            print("Invalid")
#    return name


#name = sync(name)

#if name >= 95:
#    print("'Secret route unlocked!'")
#    print("'Now i'm in control'")

#TEST 2
#name = 0

#def sync(name):
    
#    add = input("How do you feel (Happy = a), (Sad = b): ")
#    if add == "a":
#        print("good")
#        return name
#    elif add == "b":
#        print("bad")
#        name += 5
#        print(f"Your syncronisation rate is {name}")
#        return name
#    else:
#        print("wrong response")
#        return name

#name = sync(name)

#def sync1(name):
#    while name < 95:
#        try:
#            add = int(input("What is the added syncronisation rate? "))
#            name += add
#            print(f"Your syncronisation rate is {name}")
#        except ValueError:
#            print("Invalid")
#    return name

#print(".....")
#name = sync1(name)

#if name >= 95:
#    print("'Secret route unlocked!'")
#    print("'Now i'm in control'")

#TEST 3
#import sys
#import os
#import time
#def ani(word, stop = 0.5):
#    for i in word:
#        sys.stdout.write(i)
#        sys.stdout.flush()
#        time.sleep(stop)

#ani("Hi: ")
#name = input()
#print(name)

#TEST 4
#print('"hi"')

#TEST 5
#syncronisation = 0
#an=0
#def bleh(an,syncronisation):
#    print("hi")
#    syncronisation += 100
#    an+=100
#    return syncronisation
    

#syncronisation = bleh(syncronisation)

#print(syncronisation)

#def bleh2():
#    print("fail")

#bleh2()

#if syncronisation == 100:
#    print("success")
#else:
#    print("fail")

#TEST 6
#name = "hi"
#import time
#import os
#def clear_screen2():
#    time.sleep(1)
    # Check the operating system and run the appropriate clear command
#    if os.name == 'nt':  # Windows
#        os.system('cls')
#    else:  # macOS and Linux
#        os.system('clear')
#ani = print
#rc = 0
#syncronisation = 0
#def part1(rc, syncronisation):
#    ani("<Let's just start working towards a route>")
#    ani(f'"You nod your head towards {name}"')
#    ani("")
#    ani("Time to get to work player!")
#    ani("Each family has a different difficulty!")
#    ani("Brad and Joel - Easy")
#    ani("Vanessa and Mitch - Hard")
#    ani("Wei Xian - 🕈︎✋︎☹︎☹︎ ✡︎⚐︎🕆︎ ☞︎✋︎☠︎✌︎☹︎☹︎✡︎ 👍︎☹︎☜︎✌︎☼︎ 💣︎☜︎✍︎")
#    choice = 0
#    ani("Depending on which route you take, you could get endings that are... good")
#    ani("One thing though, that syncronisation rate?")
#    if syncronisation > 0:
#        a = "'Make sure it reaches 95%, you'll unlock a secret ending!'"
#        b = ":)"
#    else:
#        a = "Under NO CIRCUMSTANCES should it go anywhere near 95%, don't let it rise at all"
#        b = "Or you'll get one of the secret endings..."     
#    ani(a)
#    ani(b)
#    ani("Now it's time to explore your starting point!")
#    ani("<You look around and 3 things peak your interest...>")
#    ani("A Closet (a), A Stuffed Toy (b), A Calendar (c)")
#    ani("Which of the 3 will you explore?: ")
#        ani("<An all too familiar pin pad appears>")
#        ani("<Memories flash before your eyes>")
#        ani("<Memories of murdering the small 5 year old>")
#        ani("<Keep going>")
#        clear_screen2()
#        ani("Which numbers will you press?: ")
#        pin = int(input(""))
#        if pin == 3684:
#            ani("The Closet door opens")
#            ani("Behind the doors lies a computer")
#            ani("It is chained to the table, and seems to be struggling against its restraints")
#            ani("Release the computer? Y/N")
#            comp = input("")
#            if comp.lower() == "y":
#                ani("<You walk towards the computer not knowing what is is>")
#                ani("<Do you?>")
#                ani('"You shake your head towards the NPC"')
#                ani("<not a npc but whatever>")
#                ani("<With just a touch the chains crumble away...>")
#                ani('"..."')
#                ani("Thank you...")
#                ani("I'm sorry for ☹︎⚐︎💧︎✋︎☠︎☝︎ 👍︎⚐︎☠︎❄︎☼︎⚐︎☹︎")
#                rc = True
#                ani('"The computer disapears just as fast as it appears..."')
#                ani('"For you are no longer in the closet"')
#                ani("<You are back in the cot?>")
#                ani("<Everythings locked out, we can only move on...>")
#                ani('"Weird, I didnt know teleportation was possible in this sort of game"')
#                ani('"You make sure to not say that allowed, fearing you will incur <their> wrath"')
#                return rc, syncronisation
#            else:
#                ani("<You turn away from the computer>")
#                ani("<I've never seen it before>")
#                ani("<...>")
#                ani("<Best not risk it>")
#                ani('"As you walk out of the closet, you look back once, only to be horrified"')
#                ani("'Thanks for the help :)'")
#                syncronisation += 10
#                return rc, syncronisation
#        else:
#            ani("<Dumba$$, can't even remember the old code from last time>")
#            ani("<Can't even remember when you killed Mitch>")
#            ani('"..."')
#            ani("<It was 3684, btw>")
#            ani("<And no, we can't go back>")
#            ani('"You look down shamefully"')
#            ani("<Let's just get moving>")
#            syncronisation += 3
#            ani(f"'Syncronisation is now at {syncronisation}%'")
#            ani(" ")
#            return rc, syncronisation
#    elif c1.lower() == "b":
#        ani("<You stare at the stuffed doll>")
#        ani('"You realise that they look just like the ones we murdered last time"')
#        ani("<...part of my deal, a part of my past>")
#        ani('"..."')
#        ani("<The only gift my parents left me>")
#        ani("<Ha! Funny ain't it?>")
#        ani("<To think it was used to kill the parents that actually cared>")
#        ani('"You remain silent"')
#        ani("<Let's just go...>")
#        syncronisation += 1
#        ani(f"'Syncronisation is now at {syncronisation}%'")
#        ani("")
#        return rc, syncronisation
#    elif c1.lower() == "c":
#        ani("<You walk towards the calendar>")
#        ani("Look at the date? Y/N: ")
#        calendar = input("")
#        if calendar.lower() == "y":
#            ani("The date is 13/03/1987")
#            ani("<My birthday...>")
#            ani("<3 years before the incident>")
#            ani("<28 since you came into my life>")
#            ani("<It's also the day I got adopted>")
#            ani('"..."')
#        else:
#            ani("<Why come here if you're not even gonna look at the date???>")
#            ani("<Waste of my time...>")
#            syncronisation += 5
#            ani(f"'Syncronisation is now at {syncronisation}%'")
#            return rc, syncronisation
#    else:
#        ani("<You really are useless, we need as much information as possible!>")
#        ani('"But youve already made youre choice..."')
#    clear_screen2()

#rc, syncronisation = part1(rc, syncronisation)
#print(rc)
#print(syncronisation)

#TEST 7
#import time
#import os
#def clear_screen2():
#    print()
#    time.sleep(3)
#    # Check the operating system and run the appropriate clear command
#    if os.name == 'nt':  # Windows
#        os.system('cls')
#    else:  # macOS and Linux
#        os.system('clear')
#ani = print
#ani(f"Well , which route are you choosing?")
#ani("a) Brad and Joel")
#ani("b) Vanessa and Mitch")
#ani("c) Wei Xian")
#routechoice = 0
#while routechoice != "a" or routechoice != "b" or routechoice != "c":
#    routechoice = input("")
#    if routechoice == "a":
#        ani("bj")
#    elif routechoice == "b":
#        ani("vm")
#    elif routechoice == "c":
#        ani("wx")
#    else:
#        ani("That is not an option, please select again!")
#        routechoice = input("")
#print("done")

#TEST 8
ani = print
syncronisation = 0
syncronisation += 10
ani(f"'Syncronisation rate is at {syncronisation}% :)'")
syncronisation -= 10
ani("ERROR: SYNCRONISATION REVERSED")
ani("⧫︎♒︎♋︎■︎🙵 ⍓︎□︎◆︎📬︎📬︎📬︎")
ani(f"'Syncronisation rate is at {syncronisation}% :)'")