import sys
sys.path.append(".")
from rich import print
from ta_data.enemies.human import Human
from ta_data.src.TA_Errors import CriticalFightError, NotImplementedError

def fight(player, enemy):
    round = 0
    while player.health > 0 and enemy.health > 0:
        round += 1
        take_damage(player, enemy)
        deal_damage(player, enemy)
        
    if player.health == 0 and enemy.health > 0:
        print("[bold red]You have died to " + enemy.name +  " after " + str(round) + " rounds.")
    elif enemy.health == 0 and player.health > 0:
        print("[bold green]You have killed " + enemy.name + " after " + str(round) + " rounds. You have " + str(player.health) + " left.")
        loot(player, enemy)
    elif enemy.health == 0 and player.health == 0:
        print("[bold red]You and your enemy " + enemy.name + " habe both died in combat.")
    else:
        raise CriticalFightError("No known ending of fight " + player.name + " " + str(player.health) + " " + enemy.name + " " + str(enemy.health))

def take_damage(player, enemy):
    health_after_attack = player.health - enemy.weapon.damage
    if health_after_attack > 0:
        player.health = health_after_attack
    else:
        player.health = 0

def deal_damage(player, enemy):
    health_after_attack = enemy.health - player.weapon.damage
    if health_after_attack > 0:
        enemy.health = health_after_attack
    else:
        enemy.health = 0

def loot(player, enemy):
    try:
        raise NotImplementedError("loot is nor yet implemented")
    except NotImplementedError:
        print("looting is not yet implemented")


