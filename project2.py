
import os
import sys
from random import randint
#!/usr/bin/python3
import dice
import threading


'''Nahshon's Ongoing RPG Game'''

bestiary = [{'name': 'goblin', 'health': 10, 'damage': '1d5'},
            {'name': 'orc', 'health': 15, 'damage': '1d8'},
            {'name': 'ogre', 'health': 20, 'damage': '1d12'}]
armory = {'sword': {'damage': '1d12'}}
spell_lookup = {'fireball': {'damage': '4d6'}}
player_health = 20
inventory = []
spellbook = []


# def consequence():
#     print("You took too long! The zombie ate your brains")
#     os._exit(os.EX_OK)
#     # closes multiple-thread program


def combat():
    monster_ID = randint(0, 2)

    global player_health, inventory, armory, bestiary
    round = 1
    monster_health = bestiary[monster_ID]['health']

    print(
        f"A ferocious {bestiary[monster_ID]['name']} approaches! COMBAT HAS BEGUN!\n")
    while True:

        # S = threading.Timer(3.0, consequence)
        # S.start()

        # choices = input('what do you do?\n')
        # if choices.lower() == "run":
        # print("You escaped! YES!")
        #  S.cancel()
        #      break
        # print("You really escaped the monster")
        print(f"ROUND {round}")
        print("Player Health: [" + str(player_health) + "]")
        print("Monster Health: [" + str(monster_health) + "]")

        # gotta write code for cast
        print("Type: RUN, CAST [spell], or USE [weapon]")
        # converts move into a lower-case list to deal with each item in list separately
        move = input().lower().split()
        monster_damage = sum(dice.roll(bestiary[monster_ID]['damage']))
        print("\n=========================")

        if move[0] == 'use':
            if move[1] in inventory:  # checks if weapon is in your inventory
                player_damage = dice.roll(armory[move[1]]['damage'])
                print(
                    f"You hit a {bestiary[monster_ID]['name']} for {player_damage} damage!")
            if move[1] not in inventory:
                print(f"There is no {move[1]} in your inventory!")

        if move[0] == 'cast':
            if move[1] in spellbook:  # checks if spell is in your spellbook
                if move[1].lower() == 'fireball':
                    player_damage = sum(
                        dice.roll(spell_lookup[move[1]]['damage']))
                    print(
                        f"Summoning eldritch forces, you scorch the {bestiary[monster_ID]['name']} for {player_damage} damage!")
            if move[1] not in spellbook:
                print(f"You don't know the {move[1]} spell!")
        if move[0] == 'run':
            # + player_speed # if I set this variable later, here's where it would work
            escape_chance = randint(1, 10)

            if escape_chance >= 10:
                print("You make a flawless escape!")
                break
            if escape_chance >= 5:
                print(
                    "You expose your back as you turn and flee- the monster takes advantage.")
                print(
                    f"A {bestiary[monster_ID]['name']} hits you for {monster_damage} damage!")
                player_health -= int(monster_damage)
                if player_health >= 1:
                    print("You managed to escape.")
                    break
                if player_health < 1:
                    print("You have been slain.")
                    print("\nGAME OVER")
                    sys.exit()
            if escape_chance >= 0:
                print("The monster out-maneuvers you and attacks! You do not escape.")

        try:
            monster_health -= int(player_damage)
        except:
            pass
        if monster_health <= 0:
            print(
                f"The {bestiary[monster_ID]['name']} lies dead. You are victorious!\n")
            break

        print(
            f"A {bestiary[monster_ID]['name']} hits you for {monster_damage} damage!")
        print("=========================\n")
        round += 1
        player_health -= int(monster_damage)

        if player_health <= 0:
            print("You have been vanquished! You are dead.")
            sys.exit()


def showInstructions():
    print('''
NAHSHON'S RPG GAME
OBJECTIVE: Collect spells and weapons- fight and survive!
--------
Actions:
    GO [north, south, east, west, up, down]
    GET [item, spell]
    USE [item, spell]
    LOOK
    INV/INVENTORY

Type 'help' at any time! Type 'q' to quit!''')


def playerinfo():
    #    print('')
    # print('YOU ARE IN THE ' + currentRoom + '.')
    print('=================================')
    print('Inventory :', str(inventory))
    print('Spells :', str(spellbook))
    print('YOU ARE IN THE ' + currentRoom + '.')
    print('=================================')


def showStatus():  # display the player's status
 #   if 'desc' in rooms[currentRoom]:
 #       print(rooms[currentRoom]['desc'])
    if 'item' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'] +
              rooms[currentRoom]['item_status'] + '.')
    if 'item2' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item2'] +
              rooms[currentRoom]['item_status2'] + '.')
    if 'spell' in rooms[currentRoom]:
        print('You see a magic scroll. On the ribbon it says "' +
              rooms[currentRoom]['spell'] + '".')
#    print('=================')


def spellreceive(incantation):
 #   print("You received a new spell scroll. Be careful... magic is dangerous!")
 #   incantation = input("Create the magic word to summon your spell! >")
 #   if incantation not in spells:
    print("\nA pentagram illuminates beneath your feet as an unnatural wind sweeps your hair.")
    print("The spell has been successfully added to your spellbook. Be careful... magic is dangerous!")


def random_encounter():
    if ((int(rooms[currentRoom]['randenc'])) + 5) >= 10:
        combat()


rooms = {
    'ROOM': {
        'south': 'OPEN AREA',
        'item': 'sword',
        'item_status': ' inside of a display case. It is unlocked',
        'item2': "gun",
        'item_status2': "its a MF gun..but it doesnt do anything with out bullets",
        'randenc': '20',
        'desc': 'You are in a bedroom. There is nothing of use in this room. It stinks and everything looks crappy, but you see, to the SOUTH; an ugly OPEN AREA'
    },
    'OPEN AREA': {
        'north': 'ROOM',
        'south': 'FRONT DOOR',
        'east': 'LIVING ROOM',
        'west': 'KITCHEN',
        'randenc': '0',
        'desc': 'You are in an open area. The House has a terrible flor plan for you to see. To the WEST: a decrepit KITCHEN, To the North: a hellhole of a BEDROOM, to the SOUTH: a wooden FRONT DOOR, and to the EAST: a fugly LIVING ROOM, and I mean FUUUUUUUGGGGGGGGLLLLLY... There is nothing in this room to use.'
    },
    'FRONT DOOR': {
        'north': 'FRONT DOOR',
        'south': 'NEIGHBORHOOD',
        'randenc': '100',
        'desc': 'The only means to escape, WHAT ARE YOU WAITING FOR?!? \n OPEN IT!!!!!!'
    },
    'LIVING ROOM': {
        'north': 'MASTER',
        'south': 'GARAGE',
        'east': 'BACK DOOR',
        'west': 'OPEN AREA',
        'desc': 'A FUGLY LIVING ROOM... oh my god... THERES NO TV IN HERE! And one shaky lamp that really wont stay on... Am I being watched?!?!'
    },
    'GARAGE': {
        'north': 'LIVING ROOM',
        'south': 'NEIGHBORHOOD',
        'desc': 'A bunch of tools hanging on the wall! It smells like a bachelor apartment; loneliness, depression, a little bit of oil and a whole lot of chicken. The car in the middle is still not put together, but thats okay...',
        'item': ['sword', 'screw driver', 'candy', 'loneliness', 'depression']
    },
    'NEIGHBORHOOD': {
        'north': 'GARAGE'
    },
    'KITCHEN': {
        'west': 'PANTRY',
        'east': 'OPEN AREA',
        'spell': 'fireball',
        'desc': 'You are in a the kitchen. This where chef curry and Chef harden cooks up the defense... wait..sorry wrong kitchen. Damn, just pick up the fireball spell on the table... And is that PANTRY ajar to the left? (west)',
        'randenc': '0',
        # 'up': 'KITCHEN',
    },
    'DINING ROOM': {
        'west': 'HALL',
        'south': 'GARDEN',
        'north': 'PANTRY',
        'desc': 'You are in the dining room. The table is set for an elegant party but is covered a blanket of dust. Sleeping bats cling to the chandelier. North is a dark pantry. South lies the garden. West returns to the hall.',
        'randenc': '0',
        # 'item': 'potion',
        # 'item_status': ' hiding among the bottles of wine. It is cherry red in color'
    },
    'GARDEN': {
        'north': 'DINING ROOM',
        # 'spell': 'fireball',
        # 'randenc': '0',
    },
    'PANTRY': {
        'down': 'TRAP DOOR',
        'east': 'KITCHEN',
        'randenc': '50',
        'item': 'cookie',
        'desc': 'You are in a the pantry, with a monster... Im going to die. At least ill die with the COOKIES in here, but if i kill the monster and take the cookies... maybe ill be able to get out of here.. but Look DOWN, theres a TRAP DOOR. Or if I go EAST, im back at the Kitchen',
        'item_status': ' hiding among the bottles of wine. It is cherry red in color'
    },
    'TRAP DOOR': {
        'randenc': '100',
        'up':  'PANTRY',
        'item': 'battle axe',
        'item_status': 'The door above you will not open. You know that you are at deaths door. Grab the Axe and meet your fate. Good-Bye Adventure, Your story will be told as legend',
        'desc': 'THERES A MONSTER IN HERE!!! I wish I could go back UP to the PANTRY'

    }

}


currentRoom = 'ROOM'   # player start location

os.system('clear')  # start game with a fresh screen
showInstructions()     # show instructions to the player

while True:   # MAIN INFINITE LOOP
    playerinfo()
    showStatus()

    # ask the player what they want to do
    move = ''
    while move == '':
        move = input('>')  # so long as the move does not
        # have a value. Ask the user for inp
    # make everything lower case because directions and items require it, then split into a list
    move = move.lower().split()
    os.system('clear')  # clear the screen
    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
            if 'desc' in rooms[currentRoom]:
                print(rooms[currentRoom]['desc'])
            random_encounter()
            # if YES that direction exists, then assign your new current room to the VALUE of the key the user entered
        else:
            print("YOU CAN'T GO THAT WAY!")
    if move[0] == 'use':
        if move[1].lower() == 'potion' and 'potion' in inventory:
            print("You drink from the potion. Your health has been restored!")
            print("Your potion magically refills itself! Handy!")
            player_health = 20
    if move[0] == 'get':
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]  # add item to inventory
            # msg saying you received the item
            print(move[1].capitalize() + ' received!')
            # deletes that item from the dictionary
            del rooms[currentRoom]['item']
        elif 'item2' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item2']:
            inventory += [move[1]]  # add item to inventory
            # msg saying you received the item
            print(move[1].capitalize() + ' received!')
            # deletes that item from the dictionary
            del rooms[currentRoom]['item2']
        elif 'spell' in rooms[currentRoom] and move[1] in rooms[currentRoom]['spell']:
            spellreceive('spell')
            spellbook += [move[1]]  # add spell to spells
            del rooms[currentRoom]['spell']

        else:
            print('YOU CANNOT GET ' + (move[1].upper()) + '!')

    if move[0] == 'look':
        if 'desc' in rooms[currentRoom]:
            print(rooms[currentRoom]['desc'])  # print the look description
        else:
            print('You can\'t see anything.')

    elif move[0] == 'help':
        showInstructions()

    elif move[0] in ['q', 'quit]']:
        print("Are you sure you want to quit? Yes/No")
        quit_query = input('>')
        if quit_query.lower() in ['y', 'yes']:
            print("Thanks for playing!")
            sys.exit()
        else:
            pass

