
# Character
NAME = 0
HEALTH = 1
DAMAGE = 2
DEFENCE = 3
WEAPON = 4

# Weapons
NAME = 0
DURABILITY = 1
ATTACK = 2
DISTANCE = 3
AVAILABLE = 4

WEAPONS = (
    ["hand", -2, 30, True, True],
    ["sword", 100, 250, True, False],
    ["bow", 200, 75, False, False]
)

POSSIBLE_ENEMIES = (
    ["ork", 200, 40, 1, 0],
    ["archer", 75, 50, 1, 0]
)

ENEMY_COUNT = len(POSSIBLE_ENEMIES) - 1

PLAYER_MAX_HEALTH = 500

PLAYER = ["", PLAYER_MAX_HEALTH, 100, 5, 0]



def get_hit(enemy, attacker=PLAYER):
    weapon = attacker[WEAPON]
    counter = 0
    for i in WEAPONS:
        if counter == weapon:
            damage = i[ATTACK]
        counter += 1

    enemy[HEALTH] = enemy[HEALTH] - (damage / enemy[DEFENCE])
    if enemy[HEALTH] <= 0:
        die(enemy)


def die(character):
    if character == PLAYER:
        exit("Wasted. Try again.")
    print(character[NAME] + " is dead")


def game_rest_player():
    PLAYER[HEALTH] = PLAYER_MAX_HEALTH
    print("You were healed\nNow you have " + str(PLAYER[HEALTH]) + " hp")
