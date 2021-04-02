import sys
sys.path.append(".")
from rich import print
from random import randint
from ta_data.enemies.races import *
from ta_data.src.TA_Errors import CriticalFightError, NotImplementedError

def fight(player):
    enemy = enemy_picker()
    round = 0
    while player.health > 0 and enemy.health > 0:
        #print(round)
        round += 1
        if damage(player, enemy):
            damage(enemy, player)
        
    if player.health == 0 and enemy.health > 0:
        print("[bold red]You have died to " + enemy.name +  " after " + str(round) + " rounds.")
    elif enemy.health == 0 and player.health > 0:
        print("[bold green]You have killed " + enemy.name + " after " + str(round) + " rounds. You have " + str(player.health) + " left.")
        if player.health > 0:
            loot(player, enemy)
    elif enemy.health == 0 and player.health == 0:
        print("[bold red]You and your enemy " + enemy.name + " have both died in combat.")
    else:
        raise CriticalFightError("No known ending of fight " + player.name + " " + str(player.health) + " " + enemy.name + " " + str(enemy.health))

def damage(attacker, defender):
    if  randint(0, 100) <= attacker.weapon.accuracy:
        health_after_attack = defender.health - (attacker.weapon.damage)
        if health_after_attack > 0:
            defender.health = health_after_attack
            return True
        else:
            defender.health = 0
            return False
    else:
        return True

def loot(player, enemy):
    player.money += enemy.money
    print("You have looted", "[bold #FFD700] " + str(enemy.money) )
    try:
        raise NotImplementedError("looting asside from money looting is not yet implemented")
    except NotImplementedError:
        print("looting asside from money looting is not yet implemented")

def enemy_picker():
    return Human(randint(0,2))
