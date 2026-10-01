#A student led RPG game

#contributors
#gpoppe
#ibayraktar

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
 
    name = input ("Welcome adventurer!What is your name?: ")

    print ("Hello", name, "you have discovered a mysterious island filled with ancient secrets.")
    print ("Your goal is to find the legendary Crystal to help you escape the island.")

    print ("You arrived at a fork in the path")

    print("1. Enter the jungle")
    print("2. Climb the mountain trail")
    print("3. Follow the beach")
    choice1 = input("Which path do you choose? ")


    if choice1 == "1":
        print(name, "enters the jungle.")
    elif choice1 == "2":
        print(name, "climbs the mountain trail.")
    elif choice1 == "3":
        print(name, "follows the beach.")
    else:
        print("You got lost and the adventure ends.")
        return
# Decision 2

    print("You discover an abandoned camp with three useful items.")
    print("1. Compass")
    print("2. Flashlight")
    print("3. Rope")
    choice2 = input("Which item do you take? ")


    if choice2 == "1":
        print("You take the compass.")
    elif choice2 == "2":
        print("You take the flashlight.")
    elif choice2 == "3":
        print("You take the rope.")
    else:
        print("You waste too much time and the adventure ends.")
        return 

# Decision 3

    print("Later, you reach a rushing river.")
    print("1. Swim across")
    print("2. Build a raft")
    print("3. Search for a bridge")
    choice3 = input("What do you do? ")

    if choice3 == "1":
        print("You carefully swim across.")
    elif choice3 == "2":
        print("You build a sturdy raft.")
    elif choice3 == "3":
        print("You find an old bridge and cross safely.")
    else:
        print("You fall into the river and lose the adventure.")
        return

# Decision 4

    print("You discover the entrance to an ancient temple.")
    print("1. Enter through the main gate")
    print("2. Use a hidden side entrance")
    print("3. Climb through a rooftop opening")
    choice4 = input("How will you enter? ")

    if choice4 == "1":
        print("You walk through the massive gate.")
    elif choice4 == "2":
        print("You sneak through the side entrance.")
    elif choice4 == "3":
        print("You climb into the temple from above.")
    else:
        print("You trigger a trap and lose.")
        return

# Decision 5

    print("Inside the temple are three crystal pedestals.")
    print("1. Red Crystal")
    print("2. Blue Crystal")
    print("3. Green Crystal")
    choice5 = input("Which crystal will you take? ")

    if choice5 == "1":
        print("The temple begins to glow!")

    elif choice5 == "2":
        print("The temple begins to glow!")
    elif choice5 == "3":
        print("The temple begins to glow!")
    else:
        print("The temple collapses before you make a choice.")
        return
#Decision Treasure
    
    print ("While exploring the temple, you find a treasure chest!")
    print ("1. Open it")
    print ("2. Ignore it")
    print ("3. Inspect it carefully")

    treasurechoice = input("What do you do?")

    if treasurechoice == "1": 
        print ("You found the Golden Idol!")
    elif treasurechoice == "2": 
        print ("You leave the chest alone.")
    elif treasurechoice == "3": 
        print ("You discovered an Ancient map.")
    else: 
        print ("You walk away from the chest")
        return 

# Decision 6

    print("You must escape the island.")
    print("1. Sail away on a boat")
    print("2. Fly away in an ancient airship")
    print("3. Use a hidden portal")
    choice6 = input("How will you escape? ")

    if choice6 == "1":
        print("Congratulations", name,  "! You sail away with the Crystal of Destiny and win!")
    elif choice6 == "2":
        print("Congratulations", name, "! You fly away with the Crystal of Destiny and win!")
    elif choice6 == "3":
        print("Congratulations", name, "! You step through the portal with the Crystal of Destiny and win!")
    else:
        print("You hesitate too long and remain trapped on the island.")

# Main game loop

    play_again = input("Would you like to play again? ")

    if play_again == "yes": 
        room5()
    else: 
        print("Thanks for playing!")

    
def room6():
    #room6
    #Angela Vasquez
    print("Welcome to The Halloween Adventure Park!")

def room7():
    #room7
    print("This door is locked.")

def room8():
    #room8
    print("Welcome to the best game!")

    print ("Hello hungry traveller!")

    def game():
        name = input("Welcome! What is your name? ")
        print(name, ", you have been travelling for a long time, and you look very hungry. Your journey home has 5 stops, and the food choices you make along the way will affect your health.")
        print("Let's see how healthy you can stay by the time you get home!")

        places = ["Dominos Pizza", "McDonald's", "Subway", "Whole Foods", "Seafood Grill"]
        health_score = 0

        for stop in range(5):
            print(" ")
            print("Stop", stop + 1, "of 5: you arrive at", places[stop])

            if stop == 0:
                print("Welcome to Dominos Pizza! Our menu items are:")
                count1 = 1
                menu1 = ["Triple-cheese pizza", "Thin crust veggie-pizza", "Cauliflower dough veggie pizza"]
                for i in menu1:
                    print(count1, i)
                    count1 = count1 + 1
                select1 = int(input("Enter the item number(1-3) you want to order! :"))
                if select1 == 1:
                    print("Oh no!, too much cheese, your blood pressure will increase!")
                    health_score = health_score - 1
                else:
                    print("Great choice, healthy and yummy!")
                    health_score = health_score + 1

            if stop == 1:
                print("McDonalds! Our menu items are:")
                count2 = 1
                menu2 = ["Mc-chicken-Salad", "Triple-burger+extra cheese", "Large soda+Fries+Double cheese burger"]
                for i in menu2:
                    print(count2, i)
                    count2 = count2 + 1
                select2 = int(input("Enter the item number(1-3) you want to order! :"))
                if select2 == 1:
                    print("A chicken salad, protein and fiber, excellent choice!")
                    health_score = health_score + 1
                else:
                    print("Shall we schedule a doctor appointment for a possible heart issue!!")
                    health_score = health_score - 1

            if stop == 2:
                print("Subway! Our menu items are:")
                count3 = 1
                menu3 = ["Tuna Sandwich", "Veggie wrap", "Extra bacon + double cheese footlong"]
                for i in menu3:
                    print(count3, i)
                    count3 = count3 + 1
                select3 = int(input("Enter the item number(1-3) you want to order! :"))
                if select3 == 3:
                    print("Oh no! High cholesterol in your blood!!")
                    health_score = health_score - 1
                else:
                    print("Well done, you made a healthy and tasty choice!")
                    health_score = health_score + 1

            if stop == 3:
                print("Wholefoods! Our menu items are:")
                count4 = 1
                menu4 = ["Falafel + salad", "Lentil soup + bean salad", "Ice cream filled brownies"]
                for i in menu4:
                    print(count4, i)
                    count4 = count4 + 1
                select4 = int(input("Enter the item number(1-3) you want to order! :"))
                if select4 == 1 or select4 == 2:
                    print("Great choice, keep travelling, you have a healthy diet!")
                    health_score = health_score + 1
                else:
                    print("Come on! Is this your best choice at the Whole Foods for hunger!!")
                    health_score = health_score - 1

            if stop == 4:
                print("Seafood Grill! Our menu items are:")
                count5 = 1
                menu5 = ["Grilled tuna", "Salmon Salad", "Steamed mussels with crispy oysters"]
                for i in menu5:
                    print(count5, i)
                    count5 = count5 + 1
                select5 = int(input("Enter the item number(1-3) you want to order! :"))
                if select5 == 1 or select5 == 2:
                    print("My favorite, you have good taste buds!")
                    health_score = health_score + 1
                else:
                    print("Heads-up!, Don't eat too much and make sure they are well cooked - high parasite risk!!")
                    health_score = health_score - 1

        print(" ")
        print(name, ", you have made it home! Your final health score is", health_score)

        if health_score >= 3:
            print("You feel amazing! You are fit, full of energy, and your blood pressure is right where it should be.")
        elif health_score >= 0:
            print("You made it home okay, but a few of those choices could catch up with you. Try to eat healthier next trip!")
        else:
            print("You collapse onto the couch. The doctor says you are prediabetic and have high blood pressure. Time for a diet change!")


    play = input("Would you like to eat something?Type:  yes or no ")

    while play == "yes":
        game()
        play = input("Please enter -yes- if you are still hungry! ")
    else:
        print("Bye!")

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
    #Ceiry Molina
    #room12
    print("Ceiry's Game!")

    opt1 = ["Choose you Jedi:","1.Luke Skywalker","2.Obi Wan","3.Ahsoka"]

    opt2 = ["How do you want to eqip your compasnion:","1.Jedi Robes","2.Clome Armor","3.Mandalorian Cape"]

    opt3 = ["What mission do you want  to begin:","1.Explore a New Planet", "2.Battle the Empire","3.Attend a Galactic Celebration"]

    opt4 = ["Do you wish to upgrade your companion's Force abilities?:","1.No", "2.Increase Training","3.Master the Force"]

    opt5 = ["The Empire is attacking! How do you wish to proceed?:","1.Fight alongside your companion","2.Face the enemy alone","3.Stay back and watch"]

    opt6 = ["While on a mission you find a box! How do you wish to proceed?:","1.Open it", "2.Ignore it","3.Inspect it"]

    redo_game = ["Do you want to play again?","1.Yes","2.No"]
    again = 1 
    while(again ==1):
        print("Welcome, young Padawan! Your Star Wars adventure begins now. May the Force be with you!")

    #Level1
        for item in opt1:
            print(item)

        starter_choice = int(input("Pick a number 1-3:"))

        if starter_choice ==1:
            print("Luke Skywalker joins your journey! His courage and determination will guide you through the galaxy.")

        if starter_choice ==2:
            print("A wise choice. Obi Wan is ready to share the wisdom of the Jedi Order")

        if starter_choice ==3:
            print("Excellent choice! Ahsoka is prepared to face% any challenge and protect the galaxy")
        
        print("Before beginning your mission, let's prepare you companion!")

    #Level2
        for item in opt2:
            print(item)
    
        dress_choice = int(input("Pick a number 1-3:"))

        if dress_choice ==1:
            print("Classic Jedi style! Your companion is prepared for an honorable mission across the stars.")

        if dress_choice ==2:
            print("Battle ready! Your companion looks prepared to take on Imperial forces.")
        if dress_choice ==3:
            print("An impressive look! Your companion stands out as a true galactic hero.")

    #Level3 
        for item in opt3:
            print(item)

        journey = int(input("Pick a number 1-3:"))

        if journey ==1:
            print("Adventure awaits! Discover hidden worlds, ancient secrets, and new allies throughout7 the galaxy.")

        if journey ==2:
            print("The battle begins! Use strategy, teamwork, and the Force to defeat the Empire")

        if journey ==3: 
            print("A celebration across the galaxy! Show off your companion and enjoy the festivities")

    #Level4
        for item in opt4:
            print(item)

        evolution = int(input("Pick a number 1-3:"))

        if evolution ==1:
            print("Your companion remains as they are. Remember true strength comes from within")

        if evolution ==2:
            print("Training complete!Your companion has grown stronger and gained new Force abilities")

        if evolution ==3:
            print("Force mastery achieved! Your companion has reached their highest potential and become a legendary hero")

    #Level5

        for item in opt5:
            print(item)

        attack = int(input("Pick a number 1-3:"))

        if attack ==1:
            print("Together you fight! The force is strongest when allies stand side by side;")

        if attack ==2:
            print("Bravery is admirable, but teamwork is the Jedi way. Facing the enemy alone is risky.")

        if attack ==3:
            print("Standing aside while others fight is not the Jedi path. Heroes help those in need!")

    #Level6 

        for item in opt6:
            print(item)

        box_choice = int(input("Pick a number 1-3:"))

        if box_choice ==1:
            print("Congrats you found a purple light saber!!")

        if box_choice ==2:
            print("You leave the box alone very safe choice!")

        if box_choice ==3:
            print("You find a green light saber, very good choice!")

    #End Game 
        for item in redo_game:
            print(item)

        again = int(input("Please enter 1 or 2:"))

def room13():
    #room13
    #Muhammad Mahmood
    print("Fallout 389")

def room14():
    #room14
    # Jeff Yock
    # CTC389-151
    # Final Project
    # Best Student Ever

    qstn1 = ["Study for the test", "Play video games", "Watch TV"]
    ansr1a = ["You feel tired but you know the test is important.", "You deserve a break!", "Your hear the theme song from your favorite TV show."]
    ansr1b = ["You study a little before bed.", "You play video games until midnight.", "You go to the family room and watch TV before bed."]

    qstn2 = ["Study a litte more before school.", "Pretend to be sick.", "Make a plan to cheat."]
    ansr2a = ["You decide it might be a good idea to review more before school.", "You burp the smelliest burp you can burp.", "It's too late to study now."]
    ansr2b = ["You study a little at breakfast and in the car.", "Then you moan 'Mom. I dont feel so good.'", "You heard there's a kid at school that sells test answers."]

    qstn3 = ["Buy the cheat sheet.", "Say 'No thanks' and walk to class.", "Warn the teacher about the cheat sheet."]
    ansr3a = ["The kid says 'Five bucks, pal.'", "You shake your head, say 'No thanks,' and hurry to class.", "You hurry to the classroom and tell your teacher what happened."]
    ansr3b = ["You think it's too much money but buy it anyway.", "The kid laughs and says 'OK, enjoy your F!'", "She thanks you and says 'Hmmm, I think those cheaters will get a little surprise today.'"]

    qstn4 = ["Try to help.", "Watch and laugh.", "Go to a different bathroom."]
    ansr4a = ["You feel afraid but want to help. You say 'Stop!' and start running to go tell an adult.", "You always wanted big friends. They seem so cool.", "You feel bad but don't want any more problems today."]
    ansr4b = ["The big kids get worried, let the kid go, and run off in the other direction.", "You start laughing too and ask if you can help flush.", "You pretend you didn't see or hear anything and walk away."]

    qstn5 = ["Peek at your neighbor's test.", "Try doing the math problem on scratch paper.", "Just guess."]
    ansr5a = ["Your desk partner finished his test super fast and is smiling the biggest smile.", "You decide to try modeling the problems on scratch paper. It really helps!", "You're totally lost on this test and regret not studying."]
    ansr5b = ["He didn't cover his paper and you decide to copy all of his answers.", "You remember how to solve these kinds of problems and finish just in time.", "You just cross you fingers and start guessing."]

    def firstQ (sentName):
      print(" ")
      print(sentName, "you had a long hard day at school.")
      print("It's Thursday night and you have one day left before the weekend.")
      print("But you know that Friday is test day.")
      print("You should study but you feel super tired.")
      print("What should you do?")
      count = 1
      for i in qstn1:
        print(count, i)
        count = count + 1
      choice = int(input("Enter 1, 2, or 3: "))
      choice = choice - 1
      print(ansr1a[choice])
      print(ansr1b[choice])
      choice = choice + 1
      if choice == 1:
          points1 = 30
      elif choice == 2:
          points1 = -10
      elif choice == 3:
          points1 = 0
      return (points1)
          
    def secondQ (sentName):
      print(" ")
      print("You hear your mom calling.", sentName, "wake up! It's time for school.")
      print("You quickly get dressed but feel worried about your test")
      print("Maybe you could study a little more.")
      print("Or maybe it's time for a new plan.")
      print("What should you do?")
      count = 1
      for i in qstn2:
        print(count, i)
        count = count + 1
      choice = int(input("Enter 1, 2, or 3: "))
      choice = choice - 1
      print(ansr2a[choice])
      print(ansr2b[choice])
      choice = choice + 1
      if choice == 1:
          points2 = 20
      elif choice == 2:
          print("Your mom feels your forehead, and decides to take you to the doctor.")
          print("The doctor gives you a PAINFUL SHOT with a GIANT NEEDLE!")
          print("Now you REALLY feel sick.")
          print(" ")
          points2 = -500
      elif choice == 3:
          points2 = -30
      return (points2)

    def thirdQ (sentName):
      print(" ")
      print("When you get to school lots of kids are hanging out waiting for the gate to open.")
      print("One of the older kids sees you and walks over.")
      print("He says, 'Hey", sentName, "do you wanna buy the answers for your Math test today?'")
      print("What should you do?")
      count = 1
      for i in qstn3:
        print(count, i)
        count = count + 1
      choice = int(input("Enter 1, 2, or 3: "))
      choice = choice - 1
      print(ansr3a[choice])
      print(ansr3b[choice])
      choice = choice + 1
      if choice == 1:
          print("As soon start looking at the test answers, you feel a tap on your shoulder.")
          print("You turn around and it's the PRINCIPAL!")
          print("He takes the you and the cheat sheet straight to his office and CALLS YOUR MOM!")
          print(" ")
          points3 = -500
      elif choice == 2:
          points3 = 10
      elif choice == 3:
          points3 = 20
      return (points3)

    def fourthQ (sentName):
      print(" ")
      print("You still feel nervous about the test so you ask if you can use the restroom first.")
      print("The teacher says, 'OK", sentName, "but be quick. We are about to start the test.")
      print("You hurry out to the closest restroom but when you go in you see three older kids bullying a little kid.")
      print("They are trying to put him into the toilet. They are laughing so hard they dont see you.")
      print("What should you do?")
      count = 1
      for i in qstn4:
        print(count, i)
        count = count + 1
      choice = int(input("Enter 1, 2, or 3: "))
      choice = choice - 1
      print(ansr4a[choice])
      print(ansr4b[choice])
      choice = choice + 1
      if choice == 1:
          points4 = 10
      elif choice == 2:
          print("With all the laughing you don't notice the school safety officer come into the restroom.")
          print("You and all the big kids get SUSPENDED FOR BULLYING!")
          print("Your parents are VERY ANGRY and DISAPPOINTED.")
          print(" ")
          points4 = -500
      elif choice == 3:
          points4 = 0
      return (points4)
      
    def fifthQ (sentName):
      print(" ")
      print("It's finally time for the Math test.")
      print("You write", sentName, "on the top of your paper and begin.")
      print("It starts out easy but gets harder and harder.")
      print("You get stuck on a few problems and time is running out.")
      print("What should you do?")
      count = 1
      for i in qstn5:
        print(count, i)
        count = count + 1
      choice = int(input("Enter 1, 2, or 3: "))
      choice = choice - 1
      print(ansr5a[choice])
      print(ansr5b[choice])
      choice = choice + 1
      if choice == 1:
          print("After the test, the teacher announces she had heard there was a cheat sheet being sold on campus.")
          print("So she changed all the answers so anyone who used it would get every question wrong instead!")
          print("Your neighbor stops smiling and starts crying. They used the cheat sheet and know they got a ZERO!")
          print("And since you copied him... SO DID YOU!")
          points5 = -500
      elif choice == 2:
          points5 = 20
      elif choice == 3:
          points5 = -20
      return (points5)

    def results(score):
      if score == 100:
        print("Your grade is A+ and you made great choices today")
        print("You truly are the BEST STUDENT EVER!")
        print("Congratulations, you got the best ending!")
      elif score == 90:
        print("Your grade is A")
        print("So close! You did very good today but there is one better ending.")
      elif score == 80:
        print("Your grade is B")
        print("You did good today but there are better endings.")
      elif score == 70:
        print("Your grade is C")
        print("You did OK today but you should try again.")
      elif score == 60:
        print("Your grade is D")
        print("You barely passed! You should definitely try again.")
      elif score < 60:
        print("Your grade is F! You need to think about your choices. Try again!")
 
    print("You quickly scan the room noting the doors are all the same but the number plates are not.")  
    print("You wish you had time to make a more calculated decision but the water is rising surprisingly fast.")
    print("For some reason your eyes are drawn to the colorful plate for Room 14")
    print("Without thinking much more about it, you rush to the door, turn the handle, and enter.")
    print(" ")
    print("Closing the door behind you is diffcult as the water is rushing in, but you finally get it shut.")
    print("As you turn around, you are shocked to see a near perfect copy of your childhood bedroom.")
    print("The only difference is a bizzare object in the center of the room.")
    print("It is a smooth white cylinder about four feet tall and eight inches in diameter.")
    print("There appears to be some sort of stylus or pen sitting on top.")
    print("The base of the cylinder sits in a slight depression in a circle of small holes.")
    print("The water that entered with you is quickly draining through them.")
    print(" ")
    print("Though you feel disoriented by the room's appearance, you approach the cylinder.")
    print("Inscribed in the circular top, in colorful Comis Sans, is the following message... ")
    print("Will you play Best Student Ever? Check yes or no.")
    print("Beneath that are two crudely drawn squares that are marked 'yes' and 'no' in lower case letters.")
    print("You somehow feel it necessary to use the stylus to check one of the boxes.")

    play = input("Which box do you check? Type yes or no: ")
    if play == "no":
        print(" ")
        print("Thinking this whole situation is just too absurd, you scoff and check the 'no' box.")
        print("You instantly regret it as you hear ominous creaking getting louder from the door behind you.")
        print("As the cylinder sinks down into the depression, you notice the illusion of your childhood bedroom fading.")
        print("You turn just in time to see the door burst and the flood waters of your doom rushing in.")
      
    else:
       print(" ")
       print("Thinking that the only way out of this bizarre situation is to be proactive, you check the 'yes' box.")
       print("You feel odd as the cylinder sinks down into the depression and disappears.") 
       print("You are shocked to notice you are getting smaller and YOUNGER!")
       print("As you continue regressing, your mind gets foggy and you vaguely begin to remember a forgotton memory.")
       print("You were seven years old and were struggling with making good choices.")
       print("Your last fully cognizant thought is of a very critical day at school and a very important test.")
  
       while play == "yes":  
        score1 = 0
        score2 = 0
        score3 = 0
        score4 = 0
        score5 = 0
        scoreTot = 0
        print(" ")
        print ("Somehow you feel you've done this before...")
        print ("Never having heard of 'deja vu' at age seven, you think it's odd but otherwise ignore it.")
        print ("All week you've been lectured about good choices and bad choices.")
        print("you look at your just completed homework on your desk and notice you forgot to put your name on it.")
        print("You write your name on the top and consider what to do next.")
        plyrName = input("(Type in your name): ")
        print(" ")
        score1 = firstQ(plyrName)
        score2 = secondQ(plyrName)
        if score2 > -100:
          score3 = thirdQ(plyrName)
          if score3 > -100:
            score4 = fourthQ(plyrName)
            if score4 > -100:
              score5 = fifthQ(plyrName)
              scoreTot = scoreTot + score1 + score2 + score3 + score4 + score5
              if scoreTot < 0:
                scoreTot = 0
              print(" ")
              print ("The teacher says,'I have graded all the tests.'")
              print (plyrName, "your test score is", scoreTot)
              results(scoreTot)
              print(" ")
        play = input("Would you like to relive this day again? Type yes or no: ")
    print("Game Over")


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


