import random
import sys
import time

ans_a = ["a", "A"]
ans_b = ["b", "B"]
ans_c = ["c", "C"]
yes = ["y", "Y", "yes", "Yes"]  # response
no = ["n", "N", "no", "No"]

sword = 0  # objects
food = 0
berend = 0
bandage = 0

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.0)


def intro():
    print_slow("You went on your yearly trip to Turkmenistan like usual.\n"
          "You had made a lot of money in the past year because your small software business started doing very well so this year you went with your own private helicopter.\n"
          "After hiring a private pilot nicknamed ""Henk de Helikopterpiloot"" you would never have to fly with one of those busy planes again.\n"
          "However, whilst flying over georgia the engine started failing and you started losing altitude at an alarming rate.\n"
          "Henk de Helikopterpilot couldn't handle the stress and fainted, you didn't know how to fly a helicopter so your chance of surviving was pretty much zero.\n"
          )
    time.sleep(2)
    print("\nBang")
    time.sleep(1)
    print_slow("""
You wake up amongst the wreckage of the helicopter, you look around you and see that Henk de Helikopter has been torn apart by some sort of creature, but it seems to have left you alone
your injuries are minimal.
Do you search for life supplies?
""")
    choice = input(">>> ")

    if choice in yes:
        global food
        food = 1
        option_cliff()
    elif choice in no:
        food = 0
        option_cliff()
    else:
        print("wrong input, try again.")
        intro()


def option_cliff():
    print("\nYou continue your path towards a cliff you could see in the distance. "
          "Before you reach it, you notice a man sitting on the side of the road. "
          "Do you befriend him?  Y/N?")
    choice = input(">>> ")
    if choice in yes:
        global berend
        berend = 1  # adds a companion
    else:
        berend = 0
    if food == 0:
        print("By the time you reach the cliff, you starve to death."
              "\nShould've searched for those supplies")
        quit()
    else:
        print("\nThe cliff is too steep to climb. You keep looking around and see a cave entrance. What do you do next?")
        time.sleep(1)
        print("""A. Try climbing it anyway
B. Enter cave
    """)
    choice = input(">>> ")
    if choice in ans_a:
        print("\nReally? Your balls are this big? "
              "No one has ever managed to climb this without gear "
              "And neither wil you so...\n\nYou died!")
        quit()
    elif choice in ans_b:
            print("\nYou enter the dark mysterious cave. "
                  "Weird noises are howling in the distance "
                  "it sounds like a bear "
                  "in the alley you see a sword. To pick it up you have to solve this riddle")
            time.sleep(1)
            print("What goes up but never comes down?")
            time.sleep(1)
            print("""A. The sun 
B. Your age
C. A ball
            """)
    choice = input(">>> ")
    if choice in ans_b:
        print("You got the sword!")
        sword = 1  # adds a sword
    else:
        print("You don't have the sword, but you can still continue your trip")
        sword = 0
    print("\nWhat do you do next?")
    time.sleep(1)
    print("""A. Hide 
B. Fight
""")
    choice = input(">>> ")
    if choice in ans_a:
        print("\nYou really think that's a good idea? "
              "I'm pretty sure bears can see in the dark, and he can certainly smell you "
              "He finds you, so...\n\nYou died!")
    elif choice in ans_b:
        if sword > 0:
            print("\nIets van tekst dat je hebt gewonnen van die pauper beer "
                  " "
                  ""
                  " "
                  "\n\nYou survived!")
            option_man()
        else:  # If the user didn't grab the sword
            print("\nYou should have picked up that sword. \n\nYou died!")
    else:
        print(required)
        option_cliff()


def option_man():
    print("""you reach the cliff with berend and meet a mysterious man
    blah blah
    """)
    time.sleep(1)
    print("Mysterious man: this cliff is sacred, solve this riddle before you can climb it."
          "If you get the wrong answer, death is your penalty")
    time.sleep(1)
    print("I shave every day, but my beard stays the same. What am I?")
    time.sleep(1)
    print("""A. A barber
B. Bald
C. Beardless
                """)
    choice = input(">>> ")
    if choice in ans_a:
        print("Mysterious man: good, you're not as dumb as I thought you were. "
            "Here's a rope to go with that climbing pick you have. Good luck at the Lair")
        option_lair()
    else:
        print("Mysterious man: Too bad, I'll make it quick")
        quit()


def option_lair():
    print("You finally make it to the top."
          "Up ahead is King Julian's Lair")
    time.sleep(1)
    print("King Julian: Welcome to my lair, how can I help you?")
    time.sleep(1)
    print("iets met waarom je hier bent, en waar je heen wilt uiteindelijk")
    time.sleep(1)
    print("King Julian: To help you, I first must receive a sacrifice from you.")
    if berend == 0:
        print("You should've taken berend with you, now the only sacrifice possible was yourself.\n You die")
        quit()
    elif berend == 1:
        print("Berend: please sacrifice me, continue your adventure.")
        time.sleep(1)
        print("Berend runs away")
        time.sleep(1)
        print("King Julian: What's this?? This time I will let you solve a riddle to save yourself.")
        time.sleep(1)
        print("David’s parents have three sons: Snap, Crackle, and what’s the name of the third son?")
        time.sleep(1)
        print("""A. Pop
B. Peter
C. David
                    """)
        choice = input(">>> ")
        if choice in ans_c:
            print("King Julian: Ugh, go ahead.")
            option_maze()
        else:
            print("King Julian: It's not your lucky day, "
                  "you get executed by King Julian, you DIE")
            quit()


def option_maze():
    print("You enter the lair and see a dangerous looking man")
    time.sleep(1)
    print("What will you do?")
    time.sleep(1)
    print("""A. Talk to him
B. Ignore him
                        """)
    choice = input(">>> ")
    if choice in ans_a:
        print("Dangerous looking man: blah blah blah"
              "blah blah blah")
        time.sleep(1)
        print("What five-letter word becomes shorter when you add two letters to it?")
        time.sleep(1)
        print("""A. Seize
        B. Sharp
        C. Short
                            """)
        choice = input(">>> ")
        if choice in ans_c:
            print("Dangerous man: gives the note + directions"
                  "blah blah "
                  "in de labyrinth gaan")
        else:
            print(" Okay, you continue into the labyrinth ")
            time.sleep(1)
        print("You stumble upon a 3 way split, which way do you go? ")  # stage 1
        time.sleep(1)
        print("""A. Left
B. Right
C. Straight                     """)
        choice = input(">>> ")
        if choice in ans_a:
            print("You fall into a pit of Piranha's, you die")
            quit()
        elif choice in ans_b:
            print("You walk into a spike trap, you die")
            quit()
        else:
            print("You took the right path, now which way do you go?")  # stage 2
        time.sleep(1)
        print("""A. Left
B. Right
C. Straight                     """)
        choice = input(">>> ")
        if choice in ans_a:
            print("You get flattened by a boulder trap, you die ")
            quit()
        elif choice in ans_b:
            print("You took the right path and stumble upon a dead body. Nearby you find an apple, you put it in your backpack.\n Now which way do you go?")  # stage 3
        else:
            print("A minotaur appears and kills you")
            quit()
        time.sleep(1)
        print("""A. Left
B. Right
C. Straight                     """)
        choice = input(">>> ")
        if choice in ans_a:
            global bandage
            bandage = 1
            print("You took the right path and find a bandage, this might come in handy later. Which way will you go?")
        elif choice in ans_b:
            print("You walk into the monkey chamber, a wild BaviJari attacks you. You don't survive")
            quit()
        else:
            print("You took the right path, which way will you go now?")  # stage 4
        time.sleep(1)
        print("""A. Left
B. Right
C. Straight                     """)
        choice = input(">>> ")
        if choice in ans_a:
            print("The guard will direct you towards the exit, in return for an apple")
        elif choice in ans_b:
            print("A mummy kills you")
            quit()
        else:
            print("You step into a trapdoor, you die")
            quit()
        time.sleep(1)
        print("Not only does the guard want an apple, you have to solve a riddle to open the gate out of the maze")
        time.sleep(1)
        print("The more you take, the more you leave behind. What are they?")
        time.sleep(1)
        print("""A. Money
B. Debts
C. Footsteps
                            """)
        choice = input(">>> ")
        if choice in ans_a:
            print("WRONG, the walls start closing in on you and you die")
            quit()
        elif choice in ans_b:
            print("WRONG, the walls start closing in on you and you die")
            quit()
        else:
            print("The gate opens, you're outside and see some smoke coming up from behind a hill, civilization is close! You're nearly saved.")
            option_ending()


def option_ending():
    print("You encounter a wanderer who sees the bear hide, he asks if he could have it. Do you give it to him? Y/N")
    choice = input(">>> ")
    if choice in yes:
        print("You gain nothing but his eternal gratitude."
              "As you walk along the hills you hear a low growling noise, You look around and see the Creature that killed Henk the HelikopterPiloot")
    else:
        print("As you walk along the hills you hear a low growling noise, You look around and see the Creature that killed Henk the HelikopterPiloot")  # idk wat de bedoeling is hier? vechte ofzo


intro()

