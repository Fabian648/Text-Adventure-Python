import random, os
pathtodir = os.getcwd()
import characters
import TA_Data.src.probability
import sys
from TA_Data.src.module_ta import Logger

Logger = Logger()

state = []
x = 0
y = 5

dealerx = 0
dealery = 0
castlex = 0
castley = 0


def init(width, height):
    global y, x, state, dealerx, dealery, castlex, castley

    # Bestimmt die werte von der Burg und dem dealer so das sie nicht auf dem selben Feld stehen
    while castlex == dealerx and castley == dealery:

        dealerx = random.randint(0, width - 1)
        dealery = random.randint(0, height - 1)
        castlex = random.randint(0, width - 1)
        castley = random.randint(0, height - 1)

    for x in range(width):
        # ehemals fields
        # gegner werden in die felder gesetzt
        rows = []
        for y in range(height):
            enemies = []
            # halbiert die menge an gegnern
            for i in range(random.randint(0, 1)):
                for enemy_count in range(random.randint(0, 2)):
                    enemies.append(characters.POSSIBLE_ENEMIES[random.randint(
                        0, characters.ENEMY_COUNT)].copy())
            rows.append(enemies)
        # print(x, rows)
        state.append(rows)

    if state[dealerx][dealery]:
        state[dealerx][dealery].clear()
        state[dealerx][dealery].append("dealer")
    else:
        state[dealerx][dealery].append("dealer")

    if state[castlex][castley]:
        state[castlex][castley].clear()
        state[castlex][castley].append("castle")
    else:
        state[castlex][castley].append("castle")
    # print(state)
    # print(castlex, castley)
    # print(dealerx, dealery)


def get_enemies():
    return state[x][y]


def forward():
    global x
    if x == len(state) - 1:
        print("You see huge mountains which you can't pass")
    else:
        x += 1


def backwards():
    global x
    if x == 0:
        print("You see cliffs but you can't jump safely")
    else:
        x -= 1


def right():
    global y
    if y == len(state[x]) - 1:
        print("You see huge mountains which you can't pass")
    else:
        y += 1


def left():
    global y
    if y == 0:
        print("You see cliffs but you can't jump safely")
    else:
        y -= 1


def fight():
    enemies = get_enemies()

    while len(enemies) > 0:
        current_enemy = enemies[0]
        characters.get_hit(current_enemy)
        if current_enemy[characters.HEALTH] <= 0:
            enemies.remove(current_enemy)
            print("you killed a " + str(current_enemy[0]) + " and gathered " + str(current_enemy[5]) + " coins!")
        for enemy in enemies:
            characters.get_hit(characters.PLAYER, current_enemy)
        print("You are wounded and have " +
              str(characters.PLAYER[characters.HEALTH]) + " hp left")


def runaway():
    if probability.probability(1, 2):
        ra = random.randint(1, 4)
        print("You escaped!! But you don`t know where you are")
        if ra == 1:
            # print("You escaped!! But you don`t know where you are")
            left()
        elif ra == 2:
            # print("You escaped!! But you don`t know where you are")
            right()
        elif ra == 3:
            # print("You escaped!! But you don`t know where you are")
            forward()
        elif ra == 4:
            # print("You escaped!! But you don`t know where you are")
            backwards()

    else:
        fight()


# chech ob obj
def print_current_enemies():
    global y, x, state, dealerx, dealery, castlex, castley
    # print("You look around and see ")
    print(y, x)

    if not state[x][y]:
        return print("You look around and see nothing")
    elif x == dealerx and y == dealery:
        return print("You look around and see the dealer")
    elif x == castlex and y == castley:
        return print("You look around and see the castle")

    for enemy in state[x][y]:
        print("You are confronted by a " + enemy[characters.NAME])

    commands = {
        "fight": fight,
        "runaway": runaway
    }

    while True:
        command = input("What you wanna do? \n>").lower()

        if command in commands:
            commands[command]()
            return False

        elif command == "help":
            key = ""
            for i in commands:
                key += "-" + i + "- "
            print(key)
