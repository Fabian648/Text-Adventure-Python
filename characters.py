import os

savetime = 0
savelanguage = ""

# Character
NAME = 0
HEALTH = 1
DAMAGE = 2
DEFENCE = 3
WEAPON = 4
COINS = 5
STRENGTH = 6

PlayerFightEp = 0
nextfightlevel = 0
fightlevel = 0

# Weapons
NAME = 0
DURABILITY = 1
ATTACK = 2
DISTANCE = 3
AVAILABLE = 4
PRICE = 5

WEAPONS = (
    ["hand", -2, 30, True, True, 0],
    ["sword", 100, 250, True, False, 75],
    ["bow", 200, 75, False, False, 100]
)

POSSIBLE_ENEMIES = (
    # hier wäre ein kurze beschreibung der werte nützlich
    ["ork", 200, 40, 1, 0, 2, 0],
    ["archer", 75, 50, 1, 0, 0.5, 0]
)

skillfightlevel = {
    0: True,
    1: False,
    2: False,
    3: False,
    4: False
}

Inventory = [["sword", 100, 250, True, False]]
Hand = []

ENEMY_COUNT = len(POSSIBLE_ENEMIES) - 1

PLAYER_MAX_HEALTH = 200

PLAYER = ["", PLAYER_MAX_HEALTH, 30, 5, 0, 0, 0]

rest_available = True
rest_counter = 0
run = True


def get_hit(enemy, attacker=PLAYER):
    weapon = attacker[WEAPON]
    counter = 0
    damage = 0

    if weapon != 0:
        for i in WEAPONS:
            if counter == weapon:
                damage = i[ATTACK]
            counter += 1
    else:
        damage = PLAYER[DAMAGE]

    enemy[HEALTH] = enemy[HEALTH] - ((damage / 100 * PLAYER[STRENGTH] + damage) / enemy[DEFENCE])
    if enemy[HEALTH] <= 0:
        die(enemy)


def die(character):
    global PlayerFightEp

    if character == PLAYER:
        exit("Wasted. Try again.")

    print(character[NAME] + " is dead")
    # Abfrage ob max level
    if fightlevel != len(skillfightlevel) - 1:
        PlayerFightEp += 50
    PLAYER[COINS] += float(character[COINS])


def game_rest_player():
    global rest_counter, rest_available

    if rest_available == True:

        PLAYER[HEALTH] = PLAYER_MAX_HEALTH
        print("You were healed\nNow you have " + str(PLAYER[HEALTH]) + " hp")
        rest_available = False
        rest_counter = 5
    else:
        print("Sorry, you can't rest because the goblins are chasing you")


def skillsupdate():
    global skillfightlevel, PlayerFightEp, nextfightlevel, fightlevel

    for i in skillfightlevel:
        if skillfightlevel[i] == True:
            fightlevel = i
            nextfightlevel = i + 1

    if fightlevel != len(skillfightlevel) - 1:
        if PlayerFightEp != 0:
            if PlayerFightEp / (nextfightlevel * 200) * 100 == 100:

                PLAYER[STRENGTH] = nextfightlevel * 1.25 * 100
                skillfightlevel[nextfightlevel] = True
                PlayerFightEp = 0
                fightlevel = nextfightlevel

            elif PlayerFightEp / (nextfightlevel * 200) * 100 > 100:
                # Berechnung der übrigen EP
                resultps = PlayerFightEp / (nextfightlevel * 200) * 100
                resultps = (nextfightlevel * 200) / 100 * (resultps - 100)
                PlayerFightEp = resultps

                PLAYER[STRENGTH] = nextfightlevel * 1.25 * 100
                skillfightlevel[nextfightlevel] = True
                fightlevel = nextfightlevel


    else:
        PLAYER[STRENGTH] = fightlevel * 1.25 * 100


def skills():
    global PlayerFightEp

    os.system("cls")
    if fightlevel != len(skillfightlevel) - 1:
        print("Skills:\n\nFight:\t" + str((PlayerFightEp / (nextfightlevel * 200) * 100)) + "%\n\n\n\n")
    else:
        print("Skills:\n\nFight:\tmax. level\n\n\n\n")


def put(item):
    global run
    print(item)
    if Hand:
        for i in Hand:
            Inventory.append(i)
            Hand.clear()

    for i in Inventory:
        if i[NAME] == item:
            Inventory.remove(i)
            Hand.append(i)
    run = False


def use():
    pass


def putinv(item):
    for i in WEAPONS:
        if i[NAME] == item and item != "hand":
            Inventory.append(i)


def inv():
    global Inventory, Hand, run

    os.system("cls")
    counter = 1
    for i in Inventory:
        print(str(counter) + "\t" + i[NAME] + "\t" + str(i[ATTACK]) + " ad")
        counter += 1

    while run:
        command = input("> ").lower().split(" ")

        if len(command) > 2 or len(command) == 1:
            return print("You run around in circles and don't know what to do.")

        inv_commands = {
            "use": use(command[1]),
            "put": put(command[1])
        }

        if command[0] in inv_commands:
            inv_commands[command[0]]

    print("Your inventory was intresting!!")


def update():
    global savelanguage

    # Nur jetzt wo es eine Sprache gibt
    if savelanguage == "":
        savelanguage = "en"


def buy(item):
    global COINS

    for i in WEAPONS:

        if i[NAME] == item:
            if PLAYER[COINS] >= i[PRICE]:
                PLAYER[COINS] = int(PLAYER[COINS]) - int(i[PRICE])
                putinv(item)
            else:
                print("You have not enough money")


def help_shop():
    pass


def shop():
    os.system("cls")
    print("Shop")

    for i in WEAPONS:
        if i[NAME] != "hand":
            print(i[NAME] + "\tprice: " + str(i[PRICE]))

    while True:

        command = input(": ").lower().split(" ")

        if command == "quit":
            return False

        if len(command) > 2 or len(command) == 1:
            return print("Wrong input!!")

        buy_commands = {
            "buy": buy(command[1]),
            "help": help_shop()
        }

        if command[0] in buy_commands:
            buy_commands[command[0]]
