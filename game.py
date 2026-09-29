#A student led RPG game

#contributors
#gpoppe


#imported libraries

import math
import time

#function definitions

def room1():
    #room1
    #Ted :)
    print("Walt Disney World Vacation")

def room2():
    #room2
    print("This door is locked.")

def room3():
    #room3
    #Arpita Shah
    print("Let's Mathify this game.")

def room4():
    #room4
    #Alejandra Ibarra
    print("Pokemon Master")

def room5():
    #room5
    #Carmen Aguilar-Reyes
    print("Legendary Adventurer")

def room6():
    #room6
    #Angela Vasquez
    print("Welcome to The Halloween Adventure Park!")

def room7():
    #room7
    #Joanne Dragich
    print("Your first Ducks game!")
    #Joanne Dragich CTC389 Lab 8 Your First Ducks Game
    def playagain():
        print("Would you like to play Your First Ducks Game?")
        print("Type 1 for No and 2 for Yes.")
        play = 0
        play = int(input(">"))
        return play

    play = playagain()

    if (play == 1):
        print("Thanks for playing and let's go, Ducks!")
    while (play == 2):
        print("You exit the freeway on your way to the arena. Where do you want to park?")
        print("Type 1 - Pull into the free Katella or Cerritos parking structures.")
        print("Type 2 - Pay to park in the lot of a nearby business and walk over.")
        print("Type 3 - Pay extra for the new River parking structure.")
        parking = int(input(">"))
        if (parking == 1):
            print("It may be free, but it's super crowded. You are trapped by the traffic at the end of the game and die of starvation.")
            play = 1
            playagain()
        elif (parking == 2):
            print("You go bankrupt paying the ridiculous parking fees. Seriously, you know the structures are free, right?")
            play = 1
            playagain()
        elif (parking == 3):
            play = 1
            print("Wow, that was easy and so close. This was totally worth the money. Let's head into the arena.")
            print("Where do you head first?")
            print("Type 1 - Take a picture with Wild Wing.")
            print("Type 2 - Get a free 1st game certificate at Guest Services.")
            print("Type 3 - Check out the food court options.")
            choice2 = int(input(">"))
            if (choice2 == 1):
                print("You took a picture, but hunger made you lightheaded. You fell, hit your head, and died.")
                play = 1
                playagain()
            elif (choice2 == 2):
                print("That certificate is just a dust-catcher. Now, the food lines are super long. You die of old age waiting in line.")
                play = 1
                playagain()
            elif (choice2 == 3):
                print("Oh, wow! There are some great options here. The lines are still short this early, so you have your pick. Where do you go?")
                print("Type 1 - Hat Trick Hawaiian")
                print("Type 2 - Feather & Flame BBQ")
                print("Type 3 - El Patito Taqueria")
                choice3 = int(input(">"))
                if (choice3 == 1):
                    print("It was overpriced, and you died of food poisoning.")
                    play = 1
                    playagain()
                elif (choice3 == 2):
                    print("The liquid smoke chokes you out before you make it 10 feet.")
                    play = 1
                    playagain()
                elif (choice3 == 3):
                    print("The masa quesadilla, Red Line Margarita, and bag of churros are epic. Great choice! The game started. It's time to head to your seat.")
                    print("Type 1 - Walk right in ignoring the guard telling you to stop.")
                    print("Type 2 - Stop and talk to some Florida fans.")
                    print("Type 3 - Wait until the refs stop play to walk to your seat.")
                    choice4 = int(input(">"))
                    if (choice4 == 1):
                        print("You get hit in the head with a puck. Yeah, that rule is there because fans have gotten hurt and died.")
                        play = 1
                        playagain()
                    elif (choice4 == 2):
                        print("The Florida fans are rats just like their team. They murder you and hide the body. Your family buries an empty casket.")
                        play = 1
                        playagain()
                    elif (choice4 == 3):
                        print("The refs blow the play dead, and you walk to your seat. You have a great view!")
                        print("You're having a great time. There are 10 minutes left in the game. What do you do?")
                        print("Type 1 - Leave early to beat the traffic.")
                        print("Type 2 - Leave to buy a beer.")
                        print("Type 3 - Stay in your seat until the end.")
                        choice5 = int(input(">"))
                        if (choice5 == 1):
                            print("As you approach your car, you hear a huge roar and the goal horn. You missed the biggest goal of the season? You died of embarassment.")
                            play = 1
                            playagain()
                        elif (choice5 == 2):
                            print("A beer in the last 10 minutes? They stopped selling them after the second intermission. You hear a huge cheer and the goal horn. You missed the biggest goal of the year, and you have no beer. You died of embarassment.")
                            play = 1
                            playagain()
                        elif (choice5 == 3):
                            print("You saw the biggest goal of the year! You swear afterwards that Leo Carlsson pointed right at you during his celly. You get a high five from Wild Wing on the way out. You easily pull out of the River Garage and head home. It was the best night!")
                            playagain()
def room8():
    #room8
    print("Welcome to the best game!")

def room9():
    #room9
    print("This door is locked.")

def room10():
    #room10
    #lauren bowman
    print("The Music Career Game!")

def room11():
    #room11
    #Timothy Duong
    print("Survive a Day of Work!")

def room12():
    #Ceiry Moline
    #room12
    print("Ceiry's Game!")

def room13():
    #room13
    #Muhammad Mahmood
    print("Fallout 389")

def room14():
    #room14
    # Jeff Yock
    print("Best Student Ever")

def room15():
    #room15
    #Jitender Rajpoot
    print("Final Destination.")

def room16():
    #room16
    # Moshe Molcho
    print("Escape the Possessed Math Classroom")

def room17():
    #room17
    #Josue Zamora
    print("Two Minute Drill")

def room18():
    #room18
    #Cesar Cano
    print("Dark Gengar.")

def room19():
    #Patricia Flores
    print("Star Wars")

def room20():
    #room20
    print("This door is locked.")

def room21():
    #room21
    #Dawei Sun
    print("The Lost Jade Pendant")


def room22():
    #room22
    #Rogelio Jeronimo
    print("Playing in the Fun House.")

def room23():
    #room23
    #Mario Magallanes
    print("")
    print("Video Game Labyrinth")

def room24():
    #room24
    print("This door is locked.")

def room25():
    #room25
    print("This door is locked.")

def room26():
    #room26
    #Janelle Piva
    print("The Haunted School.")

def room27():
    #room27
    print("This door is locked.")

def room28():
    #room28
    #Vicky Kong
    print("Journey to K-Pop Concert")

def room29():
    #room29
    print("This door is locked.")

def room30():
    #room30
    #Tonya McIntyre
    print("Wise One")
    

def room31():
    #room31
    #Karl Kottman
    print("Musical Odyssey")

def room32():
    #room32
    print("This door is locked.")

def room33():
    #room33
    print("This door is locked.")

def room34():
    #room34
    print("This door is locked.")

def room35():
    #room35
    print("This door is locked.")

def room36():
    #room36
    print("This door is locked.")

def room37():
    #room37
    print("This door is locked.")

def room38():
    #room38
    print("This door is locked.")

def room39():
    #room39
    print("This door is locked.")

def room40():
    #room40
    print("This door is locked.")

def room41():
    #room41
    print("This door is locked.")

def room42():
    #room42
    print("This door is locked.")

def room43():
    #room43
    print("This door is locked.")

def room44():
    #room44
    print("This door is locked.")

def room45():
    #room45
    print("This door is locked.")

def room46():
    #room46
    print("This door is locked.")

def room47():
    #room47
    print("This door is locked.")

def room48():
    #room48
    print("This door is locked.")

def room49():
    #room49
    print("This door is locked.")

def room50():
    #room50
    #garrett poppe
    print("Game Title: Best Game Ever!")


#main program

mainChoice = 0

print("____________________________________")
print("")
print("Welcome to the role playing game!")
time.sleep(1)
print(".....")
time.sleep(1)
print("....")
time.sleep(1)
print("...")
time.sleep(1)
print("..")
time.sleep(1)
print(".")
time.sleep(1)
print("You wake up and find yourself in the center of a massive room.")
print("You do not know how you arrived here, but you look around and realize you are at the center of the room.")
print("The walls of this circular room are made of many doors.")
print("Each door has a finely crafted number plate. It appears there are 50 doors.")
print("All of a sudden, the room starts to fill with water. You must act quickly before the room floods and you drown.")
mainChoice = int(input("You decide you're going to exit through one of the doors. Which door number do you choose? "))

if mainChoice == 1:
    room1()
elif mainChoice == 2:
    room2()
elif mainChoice == 3:
    room3()
elif mainChoice == 4:
    room4()
elif mainChoice == 5:
    room5()
elif mainChoice == 6:
    room6()
elif mainChoice == 7:
    room7()
elif mainChoice == 8:
    room8()
elif mainChoice == 9:
    room9()
elif mainChoice == 10:
    room10()
elif mainChoice == 11:
    room11()
elif mainChoice == 12:
    room12()
elif mainChoice == 13:
    room13()
elif mainChoice == 14:
    room14()
elif mainChoice == 15:
    room15()
elif mainChoice == 16:
    room16()
elif mainChoice == 17:
    room17()
elif mainChoice == 18:
    room18()
elif mainChoice == 19:
    room19()
elif mainChoice == 20:
    room20()
elif mainChoice == 21:
    room21()
elif mainChoice == 22:
    room22()
elif mainChoice == 23:
    room23()
elif mainChoice == 24:
    room24()
elif mainChoice == 25:
    room25()
elif mainChoice == 26:
    room26()
elif mainChoice == 27:
    room27()
elif mainChoice == 28:
    room28()
elif mainChoice == 29:
    room29()
elif mainChoice == 30:
    room30()
elif mainChoice == 31:
    room31()
elif mainChoice == 32:
    room32()
elif mainChoice == 33:
    room33()
elif mainChoice == 34:
    room34()
elif mainChoice == 35:
    room35()
elif mainChoice == 36:
    room36()
elif mainChoice == 37:
    room37()
elif mainChoice == 38:
    room38()
elif mainChoice == 39:
    room39()
elif mainChoice == 40:
    room40()
elif mainChoice == 41:
    room41()
elif mainChoice == 42:
    room42()
elif mainChoice == 43:
    room43()
elif mainChoice == 44:
    room44()
elif mainChoice == 45:
    room45()
elif mainChoice == 46:
    room46()
elif mainChoice == 47:
    room47()
elif mainChoice == 48:
    room48()
elif mainChoice == 49:
    room49()
elif mainChoice == 50:
    room50()
else:
    print("That was the wrong choice....")
    time.sleep(1)
    print("You have perished.")


print("____________________________________")
print("")
time.sleep(1)
print(".")
time.sleep(1)
print("..")
time.sleep(1)
print("...")
time.sleep(1)
print("....")
time.sleep(1)
print(".....")
time.sleep(1)
print("You wake up and realize this was all a dream.")


