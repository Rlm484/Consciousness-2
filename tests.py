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