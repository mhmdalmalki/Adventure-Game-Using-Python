# adding time to start text one by one
import time

# adding randome to select randome objects
import random

# add here the objects lists

Zones = ['sea', 'ship', 'island']

yes_or_no = ['yes', 'no', 'y', 'n']

Weapons = ['Axe', 'iron pole', 'arrows', 'machine gun']

Sea_Creatures = ['whale', 'shark', 'octopus', 'SeaSerpent']

Island_creatures = ['Gorilla', 'Tiger', 'Corcodile', 'bear']

Ship = ['pirate', 'snakes']


# function definition here


def print_bit_pause(msg):
    print(msg)
    time.sleep(1)


def plyground():
    if choise == 'sea':
        print(random.choice(Sea_Creatures))
    if choise == 'ship':
        print(random.choice(Ship))
    if choise == 'island':
        print(random.choice(Island_creatures))
    time.sleep(3)


def changerequest():
    changerequest = input('\nwould you like to change weapon? (y/n)')
    while changerequest not in yes_or_no:
        print_bit_pause('please Enter only yes or no ..')
        changerequest = input('\nDo you want to take the other weapon? (y/n)')
    if changerequest == 'yes' or changerequest == 'y':
        weaponchoosed = random.choice(Weapons)
        print(weaponchoosed)


def wepon_use():
    use = input('Do you want to use weapen? (y/n)')
    if use == 'y' or use == 'yes':
        print_bit_pause('lets use the weapon to fight ')
    else:
        print_bit_pause('I think I will fight without my weapon ')


restart = 'yes'
while restart == 'yes' or restart == 'y':
    print_bit_pause("Welcome to the Seas Adventure game")
    print_bit_pause('where you will see extraordinaire things')
    print_bit_pause('there is three zones and many Creatures ')
    print_bit_pause('You will choose one Zone')
    print_bit_pause('and there is two weapons it will be on your way')
    print_bit_pause('be careful of your choices and try to win')
    name = input('\n\nplease Enter your name\n')
    while name.strip() == '':
        name = input('\nPlease Enter your name...\n')
    print_bit_pause('\n\nGraet lets start ... \n')
    print_bit_pause('now choose your zone..')
    choise = ''
    while choise not in Zones:
        print_bit_pause('where you want to play? ')
        print_bit_pause('please Enter (1,2,3) \n(1)sea\n(2)ship\n(3)island\n')
        choise = input()
        if choise.lower() == 'sea'.lower() or choise == '1':
            choise = 'sea'
        elif choise.lower() == 'ship'.lower() or choise == '2':
            choise = 'ship'
        elif choise.lower() == 'island'.lower() or choise == '3':
            choise = 'island'
        else:
            choise = ''
    print_bit_pause('\nlets go...')
    print_bit_pause('\nyou have find')
    weaponchoosed = random.choice(Weapons)
    print_bit_pause(weaponchoosed)
    print_bit_pause('in your way')
    changerequest()
    wepon_use()
    print_bit_pause('\nyou are now in the ' + choise +
                    ' and you have a weapon ' + weaponchoosed)
    print_bit_pause('now you see front of you')
    plyground()
    if weaponchoosed == 'machine gun':
        print_bit_pause('great you Win')
    elif weaponchoosed == 'arrows':
        print_bit_pause('great you Win')
    elif wepon_use == 'yes' or wepon_use == 'y':
        print_bit_pause('unfortunately you lose')
    else:
        print_bit_pause('unfortunately you lose')
    print_bit_pause('... Game Over')
    restart = input('play again?? (yes or no)').lower()
    while restart not in yes_or_no:
        print_bit_pause('please Enter only yes or no ..')
        restart = input('\nplay again?? (yes or no)')
