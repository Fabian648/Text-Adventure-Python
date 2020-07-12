import random
import characters

state = []
x = 0
y = 0

dealerx = 0
dealery = 0


def init(width, height):
    global y, x, state, dealerx, dealery

    dealerx = random.randint(0, width-1)
    dealery = random.randint(0, height-1)
    print(dealerx, dealery)
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


def print_current_enemies():
    global y, x, state, dealerx, dealery
    print("You look around and see ")

    if state[x][y] == []:
        return print("nothing")
    elif x == dealerx and y == dealery:
        return print("dealer")

    for enemy in state[x][y]:
        print(enemy[characters.NAME])
