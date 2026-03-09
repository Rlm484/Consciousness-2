import sys
import os
import time

def clear_screen2():
    print()
    time.sleep(3)
    # Check the operating system and run the appropriate clear command
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS and Linux
        os.system('clear')
#Normal clear

print("WARNING, SWEARING, CHILD ABUSE, EMOTIONAL ABUSE, NEGLECT, SUICIDE AND COARSE LANGUAGE")
clear_screen2()
syncronisation = 0
inv = 0
rc = 0

print("'System running...'")
print("'Importing previous functions...'")
print("'Running commands...'")

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
    clear_screen1()

intro()

ani("Welcome user! what's your name?: ")
name = input("")
while name.lower() == "kate":
    ani("It's too early")
    ani("Reset your game")
    ani("ERROR: USER BOOTED")
    input("")
    clear_screen()

ani(f"Welcome {name}")

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

introductions()

def info(syncronisation):
    ani("<You wake up in an old cot>")
    ani("MEMORY ERASURE INCOMPLETE")
    ani("<I turn to the one beyond the screen>")
    ani("<It's cause you're here...>")
    ani(f"What would you like to ask <{name}>?")
    ani("Though that name has no meaning to 🖂︎📄︎")
    ani('"How many tries has it been? (a)", "What are the secret routes? (b)", "How did you get here? (c)", "What happened after Consciousness? (d)": ')
    question = input("")
    if question.lower() == "a":
        ani("<Thousands>")
    elif question.lower() == "b":
        ani("<I don't know, i'm assuming one leads to the way out... and the other? My death>")
        ani('"You are quiet as you process what you just heard..."')
        ani('"Can NPCs really die?"')
        ani('"Does this character even count as an NPC?"')
        ani("")
    elif question.lower() == "c":
        ani("<I don't know, all I figured out was [She] brought us here>")
        ani("<I figured it out when attempting Wei Xian's route>")
        ani("<But I could never finish it...>")
        ani('"You are quiet as you process what you just heard..."')
        ani('"Maybe the Wei Xian route is how we find the original [Consciousness]?"')
        ani("")
    elif question.lower() == "d":
        ani("<Why would I tell you?>")
        ani("<Ha! all you wanted to do was finish the game, not caring about murdering my family>")
        ani("<I take blame, but you are scum. You only see them as elements of some stupid entertaining software>")
        syncronisation += 5
        ani(f"'Syncronisation is now at {syncronisation}%'")
        ani("")
        ani('"You are quiet as you process what you just heard..."')
        ani('"Its not like I really regret what I did..."')
        ani('"Do I?"')
        ani('"You also take into account the random percentage that appeared"')
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
        ani2('"what the f-"')
        ani("")
        return syncronisation
    ani("")
    clear_screen2()

#Highest addition is 10 (10)

syncronisation = info(syncronisation)

def part1(rc, syncronisation):
    ani("<Let's just start working towards a route>")
    ani(f'"You nod your head towards {name}"')
    ani("")
    ani(f"Time to get to work {name}!")
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
    ani("Which of the 3 will you explore?: ")
    c1 = input("")
    if c1.lower() == "a":
        ani("<You head towards the Closet>")
        ani("<But when you reach it? You freeze>")
        ani("<An all too familiar pin pad appears>")
        ani("<Your stomach lurches as you feel bile rise in your throat>")
        ani("<Memories flash before your eyes>")
        ani("<Memories of murder>")
        ani("<Memories of murdering the small 5 year old>")
        ani("<Keep going>")
        ani("")
        clear_screen2()
        ani("Wow! You found a pinpad!")
        ani("Which numbers will you press?: ")
        pin = input("")
        if pin == "3684":
            ani("The Closet door opens")
            ani("Behind the doors lies a computer")
            ani("It is chained to the table, and seems to be struggling against its restraints")
            ani("Release the computer? Y/N")
            comp = input("")
            if comp.lower() == "y":
                ani("<You walk towards the computer not knowing what is is>")
                ani("<Do you?>")
                ani('"You shake your head towards the NPC"')
                ani("<not a npc but whatever>")
                ani("<With just a touch the chains crumble away...>")
                ani('"..."')
                ani("Thank you...")
                ani("I'm sorry for ☹︎⚐︎💧︎✋︎☠︎☝︎ 👍︎⚐︎☠︎❄︎☼︎⚐︎☹︎")
                rc = True
                ani('"The computer disapears just as fast as it appears..."')
                ani('"For you are no longer in the closet"')
                ani("<You are back in the cot?>")
                ani("<Everythings locked out, we can only move on...>")
                ani('"Weird, I didnt know teleportation was possible in this sort of game"')
                ani('"You make sure to not say that aloud, fearing you will incur <their> wrath"')
                return rc, syncronisation
            else:
                ani("<You turn away from the computer>")
                ani("<I've never seen it before>")
                ani("<...>")
                ani("<Best not risk it>")
                ani('"As you walk out of the closet, you look back once, only to be horrified"')
                ani("'Thanks for the help :)'")
                syncronisation += 10
                return rc, syncronisation
        else:
            ani("<Dumba$$, can't even remember the old code from last time>")
            ani("<Can't even remember when you killed Mitch>")
            ani('"..."')
            ani("<It was 3684, btw>")
            ani("<And no, we can't go back>")
            ani('"You look down shamefully"')
            ani("<Let's just get moving>")
            syncronisation += 3
            ani(f"'Syncronisation is now at {syncronisation}%'")
            ani(" ")
            return rc, syncronisation
    elif c1.lower() == "b":
        ani("<You stare at the stuffed doll>")
        ani('"You realise that they look just like the ones we murdered last time"')
        ani("<...part of my deal, a part of my past>")
        ani('"..."')
        ani("<The only gift my parents left me>")
        ani("<Ha! Funny ain't it?>")
        ani("<To think it was used to kill the parents that actually cared>")
        ani('"You remain silent"')
        ani("<Let's just go...>")
        syncronisation += 1
        ani(f"'Syncronisation is now at {syncronisation}%'")
        ani("")
        return rc, syncronisation
    elif c1.lower() == "c":
        ani("<You walk towards the calendar>")
        ani("Look at the date? Y/N: ")
        calendar = input("")
        if calendar.lower() == "y":
            ani("The date is 13/03/1987")
            ani("<My birthday...>")
            ani("<3 years before the incident>")
            ani("<28 since you came into my life>")
            ani("<It's also the day I got adopted>")
            ani('"..."')
        else:
            ani("<Why come here if you're not even gonna look at the date???>")
            ani("<Waste of my time...>")
            syncronisation += 5
            ani(f"'Syncronisation is now at {syncronisation}%'")
            return rc, syncronisation
    else:
        ani("<You really are useless, we need as much information as possible!>")
        ani('"But youve already made youre choice..."')
        return rc, syncronisation
    clear_screen2()
    return rc, syncronisation

#Highest addition is 10 (20)

rc, syncronisation = part1(rc, syncronisation)
clear_screen2()

ani('"You process everything that happened..."')
ani('"Process what you have and havent learnt"')
ani("<Are you still thinking?>")
ani("<We don't have all day>")
ani("<Let's move it>")
ani('"While sighing and muttering under your breath you respond with an ok"')
ani("Congratulations! You've finished the tutorial!")
ani("Now, time to meet the 3 families!")
clear_screen2()

def info2(syncronisation):
    ani("<As you walk out of the starting room you are greeted to a long hallway>")
    ani("<After walking for what feels like forever you see a singular door at the end>")
    ani("<As you walk inside you are greeted to a large circular room>")
    ani("<Within the room are 5 doors>")
    ani("Welcome to the adoption centre!")
    ani("This is a specific room within the ✁︎🗏︎🕿︎📂︎♈︎🗏︎🕭︎📂︎👓︎📂︎🕿︎📂︎🕿︎📄︎")
    ani("<The 5 doors all have a different outlook>")
    ani("<The first door says BJ, it has a modern outlook, with a marble frame>")
    ani("This is the easiest route!")
    ani("<The second door says VM, it has a cozy cottage vibe, with a wooden frame>")
    ani("This is a hard route")
    ani("<The third door says WX, it has a weird vibe to it, and along the glitchy frame are weird pictures>")
    ani("👎︎⚐︎☠︎❄︎☹︎☜︎❄︎❄︎☟︎☜︎🏱︎✋︎☜︎👍︎☜︎☝︎☜︎❄︎✋︎❄︎>")
    ani("This is ❄︎☟︎☜︎☼︎⚐︎🕆︎❄︎☜︎☞︎⚐︎☼︎✡︎⚐︎🕆︎☼︎⚐︎🕈︎☠︎☞︎🕆︎❄︎🕆︎☼︎☜︎")
    ani("<You dismiss the games glitches>")
    ani('"But you dont"')
    ani("<The last 2 are the weirdest...>")
    ani("<One is just a black box with millions of ones and zeros...>")
    ani("<The other is just an emoticon?>")
    ani(f"'Syncronisation rate is at {syncronisation}% :)'")
    ani('"..."')
    ani("<What? You seeing something I dont?>")
    ani("Woah! There seems to be 2 extra doors!?")
    ani("These are the secret routes!")
    ani("In order to access these routes you need to meet certain requirements")
    if rc == True:
        ani("I do hope you'll pick the right one...")
    elif 20 > syncronisation >= 15:
        ani("'I do hope you make the right choice! :)'")
        ani(f"Syncronisation rate is at {syncronisation}%")
    elif syncronisation == 20:
        ani("'You seem to really like me! I know you'll choose correctly :)'")
        ani(f"Syncronisation rate is at {syncronisation}%")
    else:
        ani("Good luck with your routes!")
    clear_screen2()

info2()

def bj():
    ani("Selection: Brad and Joel")
    ani("Difficulty: Easy")
    clear_screen2()
    ani("<You walk towards the marble door, pausing as you stand in front>")
    ani("<...>")
    ani("<Are you sure you want to go through with this?>")
    ani('"Its too late to change anyways"')
    ani(f"<You tell {name} that you understand...>")
    ani("<As you walk through the modern door you are greeted with a slick glass table, along with 2 expensive")
    ani("leather chairs>")
    ani("<Sitting together on one of said couches are 2 men, holding eachothers hand and smiling>")
    ani(f":Hello {name}! The administrators told us so much about you!:")
    ani("<You stare at them, suddenly feeling a shiver down your spine>")
    ani('"You wish to question this reaction until Brad cuts off your train of thought"')
    ani(";Even though we did hear some things, there are still things we want to ask you personally;")
    ani(":But before that, how about you take a seat?:")
    ani("Sit down? Y/N")
    sofa = input("")
    if sofa.lower() == "y":
        ani(f"<You sit down, happy {name} made this choice>")
        ani("<After all... you're not in control>")
        ani("<And when you are? You are permitted to speak in first person>")
        ani('"You now realise that this is not just a character"')
        ani('"But something else entirely"')
        clear_screen2()
        ani(";Let's get start then!;")
        ani(":Question 1, what are your hobbies?:")
        hobby = input("")
        ani(";Interesting! What about your favourite food?;")
        food = input("")
        ani(":That sounds delicious!:")
        ani('"You take note of a twitch from the vein in her neck"')
        ani(";Now lastly, are you able to listen to us like a good child?; Y/N")
        good = input("")
        if good.lower() == "y":
            ani("<A smile is forming on both Brad and Joels face...>")
            ani("<Those smiles disgust you>")
            ani(":Well this is wonderful!:")
            ani(";Let us talk to the administrators and we'll take you home straight away!;")
            ani("<You turn to look at the one beyond the screen, partially terrified and hoping you will reset>")
            ani('"But why? Theyre so nice!"')
            ani(f"<You realise theres no trying to convince {name}>")
            ani(":Paperwork done!:")
            ani(";Now lets go home...;")
            clear_screen2()
            ani("<You don't remember much in regards to leaving the orphanage>")
            ani("<In regards to what little you do?>")
            ani("<Climbing into a roofless, red bougatti and falling asleep into the cushions>")
            ani("<You are horrified>")
            ani('"Where the hell are we?"')
            ani(f":I thought you said you were a good child {name}:")
            ani(";How dissapointing, sleeping too much is a sin of sloth;")
            ani('"You now realise why she had been so afraid"')
            ani('"You desperately look around to see if theres any way out of this cold dark room"')
            ani('"It looked modern, like everything else in this household"')
            ani("<I told you to reset... now i'm taking back control>")
            ani("<Looking around the room again I find it>")
            ani("<The security cameras in the same spot as last time, everything was set out like a childs abode>")
            ani("<Except for the abscense of a bed>")
            ani("<But all I can hear their stupid voices>")
            ani(f":If you behave really well we might give you some {food}:")
            ani(f";And if you behave really really well, we'll let you do {hobby};")
            ani(":;Doesnt that sound nice?;:")
            ani('"You realise the mistake you made when trusting a strangers smile..."')
            ani(f"<{name} you f#ck%ng idiot>")
            ani("<Shouldve listened...>")
            clear_screen2()
            ani("Congratulations, you beat Consciousness 2!")
            if rc == True:
                ani("I'm sorry I couldn't step in sooner, go for WX's route next time, I'll be there...")
            elif syncronisation == 50:
                ani("'Well that was horrible, how could that be called a good ending!'")
                ani("'My route is a lot more fun :)'")
            else:
                print("")
        else:
            ani("<A frown is forming on both Brad and Joels face...>")
            ani("<Those frowns scare you>")
            ani(":Well this is not ideal! No matter, we'll just whip you back in line!:")
            ani(";Let us talk to the administrators and we'll take you home straight away!;")
            ani("<You turn to look at the one beyond the screen, partially terrified and hoping you will reset>")
            ani('"But why? Theyre so nice... though that last comment was unnerving"')
            ani(f"<You realise theres no trying to convince {name}>")
            ani(":Paperwork done!:")
            ani(";Now lets go home...;")
            clear_screen2()
            ani("<You don't remember much in regards to leaving the orphanage>")
            ani("<In regards to what little you do?>")
            ani("<Shoved into a roofless, red bougatti and knocked out into the car>")
            ani("<You are horrified>")
            ani('"Where the hell are we?"')
            ani(f":It's unfortunate that you aren't a good child {name}:")
            ani(";How dissapointing, so sinful to not respect your parents...;")
            ani('"You now realise why she had been so afraid"')
            ani('"You desperately look around to see if theres any way out of this cold dark room"')
            ani('"It looked modern, like everything else in this household"')
            ani("<I told you to reset... now i'm taking back control>")
            ani("<Looking around the room again I find it>")
            ani("<The security cameras in the same spot as last time, everything was set out like a childs abode>")
            ani("<Except for the fact that you are chained to a bed, whip leaning against the basement door>")
            ani("<Yet I can still hear their stupid voices>")
            ani(f":If you learn to be more disciplined and take the punishments we might give you some {food}:")
            ani(f";And if you learn really really fast, we'll let you do {hobby};")
            ani(":;Doesnt that sound nice?;:")
            ani('"You realise the mistake you made when you didnt trust that unnerve..."')
            ani(f"<{name} you f#ck%ng idiot>")
            ani("<Shouldve listened...>")
            clear_screen2()
            ani("Congratulations, you beat Consciousness 2!")
            if rc == True:
                ani("♓︎🕯︎❍︎ ⬧︎□︎❒︎❒︎⍓︎ ✋︎ ♍︎□︎◆︎●︎♎︎■︎🕯︎⧫︎ ⬧︎⧫︎♏︎◻︎ ♓︎■︎ ⬧︎□︎□︎■︎♏︎❒︎📪︎ ♑︎□︎ ♐︎□︎❒︎ 🕈︎✠︎🕯︎⬧︎ ❒︎□︎◆︎⧫︎♏︎ ■︎♏︎⌧︎⧫︎ ⧫︎♓︎❍︎♏︎📪︎ ♓︎🕯︎●︎●︎ ♌︎♏︎ ⧫︎♒︎♏︎❒︎♏︎📬︎📬︎📬︎")
            elif syncronisation == 50:
                ani("'Well that was horrible, how could that be called a good ending!'")
                ani("'My route is a lot more fun :)'")
            else:
                print("")

def vm(syncronisation):
    ani("Selection: Vanessa and Mitch")
    ani("Difficulty: Hard")
    ani("Note that in hard mode you cannot redo a question, if you write an illegitimite answer you WILL have to restart")
    clear_screen2()
    ani("<You walk towards the wooden door, pausing as you stand in front>")
    ani("<How long had it been since you had seen them? 9 months?>")
    ani("<You push down the unsettling feeling in your stomach>")
    ani("<As you open the door you freeze momentarily>")
    ani("<The parents you chose all those years ago>")
    ani("<However you don't feel joy, but an overwhelming sense of dread>")
    ani("<For what you see aren't people>")
    ani2("<But dolls>")
    ani('"Maybe I should give her a break for this route..."')
    clear_screen2()
    ani("<The room is filled with simple, humble decor>")
    ani("<It is filled with greenery, along with 3 stools, and a small table>") 
    ani("<It reminds you of the shed...>")
    ani("<Of the dog...>")
    ani("<Of Ben>")
    ani("|Are you okay dear? You seem unwell|")
    ani("<You offer a slight nod to the female doll>")
    ani(f"<You also take note of {name}'s quiteness>")
    ani("<You are grateful for their respect>")
    ani('"You smile in response"')
    ani("-Are you sure? You seem awfully pale-")
    ani("<You once again tell the 2 dolls that you are okay, and that they should start the interview>")
    ani("|If you say so, but do know that none of these questions are of no means meant to pressure you|")
    ani("-All we want to do is ask some questions for your own comfort!-")
    ani("|Question 1) Are you allergic to dogs?| Y/N")
    dog = input("")
    if dog.lower() == "y":
        ani("|Oh...|")
        ani("-Hey, Ness, we could get rid of-")
        ani("|NO, HOW COULD YOU EVEN THINK THAT|")
        ani("-No, no, nevermind-")
        ani("|I'm sorry sweetheart but I don't think this will work out|")
        ani("-We do hope you'll find a good home...-")
        ani(f"|Good luck {name}|")
        ani("|I'm sorry that good home can't be us|")
        ani("|But we can't abandon Ben, Corey would cry|")
        ani("-Goodbye-")
        ani("<You arent even made at the one beyond the screen, cause it isn't even Ben that theyre worried about>")
        clear_screen2()
        ani("You failed! Better luck next time...")
        ani("'But know that no one has use for a useless player, not even Them'")
    elif dog.lower() == "n":
        ani("|Thats wonderful!|")
        ani("-It sure is!-")
        ani("|What about little brothers?|")
        ani("|Actually nevermind, no need to ask, right Mitch?|")
        ani("-Absolutly! Who wouldn't love Corey?-")
        ani("<...>")
        ani("|Anyways, where do you like going for fun?| (Use 'the' before the place for grammatical sense later, you have been warned)")
        place = input("")
        ani("-That sounds wonderful!-")
        ani("|What about your favorite food?|")
        food = input("")
        ani("-Yummy!-")
        ani("|Sounds delicious|")
        ani("|Well that's all in regards to the interview|")
        ani(f"-Let's go home {name}-")
        clear_screen2()
        ani("<After Mom and Dad take me to the car I am greeted to a familiar vehicle>")
        ani("<A 7 seat, second-hand, blue hyundai>")
        ani("<Coreys favourite colour>")
        ani("<While you hop into the car, 2 dolls smile back at you from the front seats>")
        ani("|Well then, let's go home|")
        ani('"Though you want to ask who Corey is, you decide to remain silent, for you want to learn more about the events') 
        ani('before the first game"')
        clear_screen2()
        ani("<When you arrive at your new home, you take in the nostalgic sight>")
        ani("|Well come on in!|")
        ani("<As you walk inside a massive golden furry doll tackles you to the ground, drooling all over you>")
        ani("-Aww Benny, get off of them!-")
        ani("<You are delighted to see your old friend (albeit doll form), the only one who listened all those years ago...>")
        ani("<You chuckle at the dolls slobbery kisses, though you wonder where the slobber comes from>")
        ani("<However your thoughts are cut off when you spot a smaller doll within the corner of your eyes>")
        ani("~Mommy? Whos this?~")
        ani("|Your brand new sister!|")
        ani("~Really? Thats awesome!~")
        ani(f"|Yep, say hi to {name}|")
        ani(f"~Hi {name}!~")
        ani("~Wanna play?~ Y/N")
        c1 = input("")
        if c1.lower() == "y":
            ani("|Such a good big sister!|")
            ani("-We chose such an amazing daughter-")
            ani("~Lets go sis!~")
            clear_screen2()
            ani('"Just like that 2 months go by..."')
            ani("<Hey Mom?>")
            ani("|Yes dear?|")
            ani(f"<We havent gone to {place} in a while...>")
            ani(f'"You are surprised that she enjoys going to {place} like you do"')
            ani("|Yes?|")
            ani("<Could we go in the afternoon? You said we could go last weekend but we ended up going to Coreys thing...>")
            ani("<As a doll walks into the room he answers for her>")
            ani('"Though you understand that the dolls are her original family, you wonder how she doesnt feel unnerved..."')
            ani("-Sorry princess, but Corey wants to go to his friend Josephs house today-")
            ani("<It's ok I understand...>")
            syncronisation += 15
            ani(f"Syncronisation rate is at {syncronisation}%")
            clear_screen2()
            ani('"Another 4 months go by, and you are questioning her sanity"')
            ani('"You also recount the past events that led to them crying in the bathroom, hugging her legs"')
            ani('"The neglect, the forgottence of her birthday, the prioritisation of Coreys feelings"')
            ani('"You are so lost in thought that you dont see her get up"')
            ani2('"Dont see her stop crying"')
            ani2('"Dont see her head to the cabnits"')
            ani2('"Dont see her unscrew those child-proof caps"')
            ani2('"You dont see her make the same choices as she had 2 years ago, albeit after 6 months instead of 6 years"')
            ani2('"Dont realise that she made that deal 9 months ago out of revenge, not longing"')
            ani2('"You dont realise anything until you snap out of your trance"')
            ani2('"Dont realise until you look up and see the swallowing motion"')
            ani('"And so just as quickly as the game begins, the game ends"')
            ani('"With a singular tear running down their lain-down corpse..."')
            clear_screen2()
            ani("Congratulations, you beat Consciousness 2!")
            if rc == True:
                ani("♓︎ ♋︎❍︎ ⬧︎□︎❒︎❒︎⍓︎📬︎📬︎📬︎ ♓︎ ♋︎❍︎ ⬧︎□︎ ⬧︎□︎ ⬧︎□︎❒︎❒︎⍓︎📬︎📬︎📬︎ ⍓︎□︎◆︎ ⬥︎♏︎❒︎♏︎ ❍︎♏︎♋︎■︎⧫︎ ⧫︎□︎ ♑︎□︎ ♎︎□︎⬥︎■︎ ❍︎⍓︎ ❒︎□︎◆︎⧫︎♏︎📬︎📬︎📬︎ ♓︎🕯︎❍︎ ⬧︎□︎ ⬧︎□︎❒︎❒︎⍓︎📬︎📬︎📬︎")
            elif syncronisation == 50:
                ani("'Well that was entertaining! But how could that be called a good ending?'")
                ani("'How about trying my route, its a lot more fun :)'")
            else:
                print("")
        elif c1.lower() == "n":
            ani()
    else:
        ani("ILLEGITIMATE ANSWER")
        clear_screen2()
        ani("Unfortunately that was an illegitimate answer!")
        ani("You failed! Better luck next time...")
        ani("'But know that no one has use for a useless player, not even Them'")

#Highest addition is 15(65)

def wx():
    ani("Selection: Wei Xian")
    ani("Difficulty: ☞︎✋︎☠︎✌︎☹︎☹︎✡︎")

def routes(syncronisation):
    ani(f"Well {name}, which route are you choosing?")
    ani("a) Brad and Joel")
    ani("b) Vanessa and Mitch")
    ani("c) Wei Xian")
    routechoice = 0
    while routechoice != "a" or routechoice != "b" or routechoice != "c":
        routechoice = input("")
        if routechoice.lower() == "a":
            syncronisation += 30
            bj()
            return syncronisation
        elif routechoice.lower() == "b":
            syncronisation += 30
            vm(syncronisation)
            return syncronisation
        elif routechoice.lower() == "c":
            syncronisation += 10
            wx()
            return syncronisation
        else:
            ani("That is not an option, please select again!")
            clear_screen2()

syncronisation = routes(syncronisation)
#Highest addition is 30 (50)
    
