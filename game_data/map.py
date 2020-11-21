import random
import characters
import probability
import sys
import Backup_py

Logger = Backup_py.Logger()

state = []
x = 0
y = 0

dealerx = 0
dealery = 0
castlex = 0
castley = 0


def init(width, height):
    global y, x, state, dealerx, dealery, castlex, castley

    run = True

    while run:

        dealerx = random.randint(0, width - 1)
        dealery = random.randint(0, height - 1)
        castlex = random.randint(0, width - 1)
        dealery = random.randint(0, height - 1)

        if not castlex == dealerx and castley == dealery:
            run = False

    for x in range(width):
        fields = []
        for y in range(height):
            enemies = []
            for enemy_count in range(random.randint(0, 2)):
                enemies.append(characters.POSSIBLE_ENEMIES[random.randint(
                    0, characters.ENEMY_COUNT)].copy())
            fields.append(enemies)

        state.append(fields)

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
        for enemy in enemies:
            characters.get_hit(characters.PLAYER, current_enemy)
        print("You are wounded and have " +
              str(characters.PLAYER[characters.HEALTH]) + " hp left")


def runaway():
    if probability.probability(1, 2):
        ra = random.randint(1, 4)
        if ra == 1:
            print("You escaped!! But you don`t know where you are")
            left()
        elif ra == 2:
            print("You escaped!! But you don`t know where you are")
            right()
        elif ra == 3:
            print("You escaped!! But you don`t know where you are")
            forward()
        elif ra == 4:
            print("You escaped!! But you don`t know where you are")
            backwards()
    else:
        fight()


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
        "quit": lambda: Logger.all_log("Exit code 2" + Logger.lineno()) + sys.exit(print("You commit suicide in front "
                                                                                         "of our opponent's and leave "
                                                                                         "this world.")),
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
