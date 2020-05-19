# Interstate 80: txt adventure game
# Wade Costa
import math
import random
import os
import time
import sys


screen_width = 100
hours = 48
health = 100
name = ''
gender = ''


# Player Dies Function
def dead():
    print('\n')
    print('-'*5 + 'Game OVER!' + '-'*5)
    print('You Are Dead')
    print('Play Again')
    sys.exit()

# Player Sleeps; Losses hours, Regains health
def sleep():
    os.system('cls')
    global hours
    global health
    if (health == 100):
        print("No need to sleep. You already have max health.")
    else:
        print('For each hour that you sleep, you will regain 10 health.')
        print("You current health is:", health)
        print("How many hours do you want to sleep for?: ")
        sleep = int(input("> "))
        hours = hours - sleep
        health = health  + (10*sleep)
        if health > 100:
            health = 100
            print("You over slept.")
        print("Now your current health is:", health)

# Player Gets Attacked And Losses (1 to 10) health points
def attack():
    os.system('cls')
    global health
    number = random.randint(1,30)
    health = health - number
    if health > 0:
        print('You have won this battle')
    else:
        dead()
    print('Health Remaining:' , health)

# Road Stop
def roadStop():
    os.system('cls')
    global health
    print("\n" + "You have entered a road stop.")
    print("You have " , health , " health" )
    print("Would you like to sleep? ")
    playerInput = input("> ")
    if playerInput.lower() == 'yes':
        sleep()

def checkDead():
    global hours
    global health
    if hours <= 0:
        dead()
    elif health <= 0:
        dead()


#-------------------main------------------------------------------------------------

# Start in San Francisco
# Begining / Waking Up

######## Startup ########

### Title Screen ###
def titleScreenSel():
    global name
    global gender
    option = input("> ")
    if option.lower() == ("play"):
        print("\n"+"What's your name?")
        name = input("> ")
        time.sleep(1)
        print('\n'+"Are you a Male or Female")
        mf = input('> ')
        if mf.lower() == ('female'):
            gender = ('her')
        elif mf.lower() == ('male'):
            gender = ('his')
        while mf.lower() not in ['female', 'male']:
            print("Please enter a valid command.")
            mf = input("> ")
            if mf.lower() == ('female'):
                gender = ('her')
            elif mf.lower() == ('male'):
                gender = ('his')
    elif option.lower() == ("help"):
        helpMenu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            print("What's you name?")
            name = input("> ")
        elif option.lower() == ("help"):
            helpMenu()
        elif option.lower() == ("quit"):
            sys.exit()

def titleScreen():
    os.system('cls')
    print('#' * 42)
    print('# Welcome to I-80: A txt Adventure Game! #')
    print('#' * 42)
    print('\n'+'- Created By: Wade Costa' + '\n')
    print('- Play -')
    print('- Help -')
    print('- Quit -' + '\n')
    titleScreenSel()

def helpMenu():
    print('#' * 42)
    print('# Welcome to I-80: A txt Adventure Game! #')
    print('#' * 42)
    print('- Use the number keys to make your decisions')
    print('- You have 48 hours to reach the end or else you die!')
    print('- You start off with 100 health points and will loss points in battle')
    print('- Sleeping at stops is how you regain health points')
    print("- Good luck and don't die!")
    print("- Type 'play' to begin or 'quit' to quit the game.")
    titleScreenSel()


##### GAME PLAY ####
#def startGame():




###### MAP ########

#DESCRIPTION = 'description'
#EXAMINATION = 'examine'
#SOLVED = False
#solvedPlaces = {'sf': False, 'sac': False, 'slc': False, 'che': False,
#                'dav': False, 'cha': False, 'gary': False, 'ross': False,
#                'tea': False
#                }


####################### Main #########################################################3

# Start Function
def woke():
    global health
    global hours
    os.system('cls')
    print(name + ' hears a loud "BOOM!" and opens ' + gender + ' eyes.')
    time.sleep(2)
    print('You see your two friends: Bob and Jay.')
    time.sleep(2)
    print('Jay : "Get up loser... We have to leave.')
    time.sleep(2)
    print(name + ' : "Wait... What is happening?')
    time.sleep(2)
    print('Jay : "There is no time to explain!')
    time.sleep(2)
    print('\n' + "You have two options")
    time.sleep(1)
    print("1.) Listen to Jay and follow his directions.")
    time.sleep(1)
    print("2.) Go back to sleep.")
    rand = random.random()
    time.sleep(1)
    print("Type '1' or '2'")
    playerInput = input("> ")
    if playerInput == '1':
        print ("Good option. You survived.")
    elif (playerInput == '2' and rand >= 0.5):
        print('\n' + "While sleeping... Jay carried you out of the house." + '\n' +
               "But hurt your arm on the way out.")
        time.sleep(5)
        health = health - 30
    else:
        dead()
    print(hours, health)




titleScreen()

time.sleep(2)

# begin
woke()


# Road Stop One
if health < 100:
    roadStop()



# Sacramento, CA

def citySac():
    global health
    ran = random.random()
    print('\n' + name + " arrived in Scramento, CA. The state capital of California")
    time.sleep(2)
    print(name + " can't continue of the interstate because " + name + " sees a bunch of busses blocking the interstate")
    time.sleep(2)
    print(name + " sees a bunch if aliens peaking out the windows of the busses.")
    time.sleep(2)
    print("1.) Do you act dead" + '\n' + "2.) Or do you fight back?")
    playerInput = input("> ")
    if playerInput == '1':
        print("Smart move.... You'll survive at least a few more hours.")
    elif(playerInput == '2' and ran >= 0.5):
        attack()
    else:
        print("Before " + name + " could fight... an alien saw " + name + " land leveled your car with a single blast!")
        dead()
    os.system('cls')
    print(name + " sees a bunch of soldiers come out behind the busses... ")
    time.sleep(2)
    print("The lead soldier comes up to " + name)
    time.sleep(2)
    print("Wolf : Hello my name is Wolf and we are part of the resistance!")
    time.sleep(2)
    print(name + " : The resistance ?")
    time.sleep(2)
    print("Wolf : Yes! We are fighing back against the aliens.")
    time.sleep(2)
    print(name + " : Can we help ?")
    time.sleep(2)
    print("Wolf : Hahaha... nope. You are too weak but you can come with me to our base")
    print("Do you want to go the base: 'yes' or 'no'")
    time.sleep(2)
    playerInput = input("> ")
    if playerInput.lower == "yes" or "y":
        print("You arrived at the resistance's base")
        print("Would you like to sleep")
        playerInput = input("> ")
        if playerInput.lower() == ("yes" or "y"):
            print("You woke up to find aliens eating your body")
            dead()
        os.system('cls')
        print("Wolf : HAHAha!!!")
        time.sleep(2)
        print("Bob : Why are you laughing???")
        time.sleep(2)
        print("Because you are on the menu :)")
        time.sleep(2)
        print("Jay : WHAT!?!")
        time.sleep(2)
        print("Wolf : Since food is limited..... ")
        time.sleep(2)
        print("Wolf : We needed a new source of food... Dumb weak human")
        time.sleep(2)
        print(name + " : We need to leave")
        time.sleep(2)
        print("Wolf : No one is leaving here alive")
        time.sleep(2)
        ran = random.random()
        if ran >= 0.5:
            attack()
            checkDead()
        else:
            dead()
        print(name + " killed Wolf and escaped through the vents to the outside")
        time.sleep(2)




def aroundSac():
    global hours
    os.system('cls')
    hours = hours - 10
    print("You took the long way but advoided many battles throughout the city")

os.system('cls')

print(name + " sees a sign that states that Scramento is 5 miles ahead")
time.sleep(2)
print("Bob : We should take the back road and advoid the city")
time.sleep(2)
print("Jay : I think that it will be no big deal to go through the city")
time.sleep(2)
print("Bob : Sacramento is most likely full of aliens and people and going around the city will only take a few more hours.")
time.sleep(2)
print("Do you chose to go 'around' the city or 'through' the city")
playerInput = input("> ")
if playerInput.lower() == 'around':
    aroundSac()
elif playerInput.lower() == 'through':
    citySac()
while playerInput.lower() not in ['around','through']:
    print("Please enter a valid command.")
    playerInput = input("> ")
    if playerInput.lower() == ("around"):
        aroundSac()
    elif playerInput.lower() == ("through"):
        citySac()



# Salt Lake City, UT  #################### FIX
os.system('cls')
print(name + " sees a sign that Salt Lake City is 5 miles ahead")
time.sleep(2)
print("You use your binoculars that happen to be in your car and see")
time.sleep(2)
print("and see a wall surrounding the city and soldiers patrolling the area ahead.")
time.sleep(2)
print("You see that there is a back road and ")


# Cheyenne, WY
os.system('cls')
print("Welcome to Cheyenne")
time.sleep(2)
roadStop()
time.sleep(2)
print("You see aliens")
attack()


# Davenport, IA
os.system('cls')
print(name + " entered Daveport")
time.sleep(2)
choice = input("Would you like to sleep?: ")
if choice.lower == ('yes' or 'y'):
    sleep()



# Channahon, IL
os.system('cls')
print("Welcome to Channabon")
time.sleep(2)
roadStop()
time.sleep(2)
print("You see aliens")
attack()

# Gary, IN
os.system('cls')
print("Welcome to Gary")
time.sleep(2)
roadStop()
print("You see aliens")
time.sleep(2)
attack()


# Rossford, OH
os.system('cls')
print("Welcome to Rossford")
time.sleep(2)
roadStop()
print("You see aliens")
time.sleep(2)
attack()



# Teaneck, NJ
os.system('cls')
print("Welcome to Teaneck")
time.sleep(2)
roadStop()
print("You see aliens")
time.sleep(2)
attack()

checkDead()
os.system('cls')
print("You Won!")
print("Good Job")
print(name + " finished with " + hours + " hours left and " + helth + " left")
