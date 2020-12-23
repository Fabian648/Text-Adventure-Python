import os, sys
from TA_Data.src.module_ta import Logger
Logger = Logger()

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
SKILLS = []
# Noch nicht inplementiert
INVENTORY = []

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
    # NAME HEALTH DAMAGE DEFENCE WEAPON COINS STRENGTH
    ["ork", 200, 40, 1, 0, 2, 0],
    ["archer", 75, 50, 1, 0, 0.5, 0]
)

# Welches Skill Level ist ereicht
skillfightlevel = {
    0: True,
    1: False,
    2: False,
    3: False,
    4: False
}

Inventory = [["sword", 100, 250, True, False]]
itemname = "sword"
Hand = []

ENEMY_COUNT = len(POSSIBLE_ENEMIES) - 1

PLAYER_MAX_HEALTH = 200

PLAYER = ["", PLAYER_MAX_HEALTH, 30, 5, 0, 0, 0, 0]

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

    if rest_available:

        PLAYER[HEALTH] = PLAYER_MAX_HEALTH
        print("You were healed\nNow you have " + str(PLAYER[HEALTH]) + " hp")
        rest_available = False
        rest_counter = 5
    else:
        print("Sorry, you can't rest because the goblins are chasing you")


def skillsupdate():
    global skillfightlevel, PlayerFightEp, nextfightlevel, fightlevel

    for i in skillfightlevel:
        if skillfightlevel[i]:
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


def invenv_put(item):
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


def invenv_use(item):
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
            "use": invenv_use(command[1]),
            "put": invenv_put(command[1])
        }

        if command[0] in inv_commands:
            inv_commands[command[0]]

    print("Your inventory was intresting!!")


def update():
    global savelanguage

    # Nur jetzt wo es eine Sprache gibt
    if savelanguage == "":
        savelanguage = "en"


def buy():

    global COINS

    def buy_item():
        item = input("Item that you want to buy : ").lower()
        if item in WEAPONS:
            return item
        elif item == "quit" or item == "leave":
            return False
        elif item == "help":
            print("enter the name of the item you want to buy or -quit- to leave the shop")
            buy_item()
        else:
            print("This item doesn't exist.")
            buy_item()

    buy_item_name = buy_item()
    if buy_item_name:

        for i in WEAPONS:

            if i[NAME] == buy_item_name:
                if PLAYER[COINS] >= i[PRICE]:
                    PLAYER[COINS] = int(PLAYER[COINS]) - int(i[PRICE])
                    putinv(buy_item_name)
                    print("you bought " + buy_item_name + "and stored it in your backpack")
                    return True
                else:
                    print("You don't have not enough money")
                    return True

    elif not buy_item_name:
        return False
    else:
        Logger.all_log("Error code 2 in shop.py" + Logger.lineno())
        sys.exit("Exit code 3")


def help_shop():
    helper = ""
    for i in shop_commands:
        helper += "-" + i + "- "
    print(helper)
    return True


def shop_quit():
    return False


shop_commands = {
    "buy": buy,
    "help": help_shop,
    "quit": shop_quit
        }


def shop():

    os.system("cls")
    running_shop_loop = True
    print("Shop \nYour coins = " + str(PLAYER[5]))

    for i in WEAPONS:
        if i[NAME] != "hand":
            print(i[NAME] + "\tprice: " + str(i[PRICE]))

    while running_shop_loop:

        shop_command = input(": ").lower()

        if shop_command in shop_commands:
            running_shop_loop = shop_commands[shop_command]()

            if running_shop_loop:
                True

            elif not running_shop_loop:
                print("You Leave the shop")

            else:
                Logger.all_log("Error code 2 in shop.py" + Logger.lineno())
                sys.exit("Exit code 3")

        else:
            print("this command is invalid. Type -help- to see the shop commands. ")
