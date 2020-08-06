import random
import map
import characters
from configparser import ConfigParser
import time
from pathlib import Path

cfg = ConfigParser()

interim = 0


def game_help():
    print(commands.keys())


def fight():
    enemies = map.get_enemies()
    while len(enemies) > 0:
        current_enemy = enemies[0]
        characters.get_hit(current_enemy)
        if current_enemy[characters.HEALTH] <= 0:
            enemies.remove(current_enemy)
        for enemy in enemies:
            characters.get_hit(characters.PLAYER, current_enemy)
        print("You are wounded and have " +
              str(characters.PLAYER[characters.HEALTH]) + " hp left")



def load():

    namedata = input("Please enter the name: ")
    data = "Config_TA_" + namedata + ".txt"
    cfg.read(data)

    characters.PLAYER[characters.NAME] = cfg.get("config_TA", "player")
    characters.savelanguage = cfg.get("config_TA", "language")
    characters.PLAYER[characters.COINS] = float(cfg.get("config_TA", "coins"))
    characters.savetime = float(cfg.get("config_TA", "time"))
    characters.PLAYER[characters.HEALTH] = float(cfg.get("config_TA", "HP"))

def save():
    global interim
    #von Datei time rauslesen wenn sie exestiert

    tosavetime = interim + characters.savetime

    cfg["config_TA"] = {"Player": characters.PLAYER[characters.NAME],
                        "language": "en", "coins": characters.PLAYER[characters.COINS], "time": tosavetime, "HP": characters.PLAYER[characters.HEALTH]}
    cfg["config_Game"] = {}#Rest Zeit usw. Map Größe

    with open("Config_TA_"+ characters.PLAYER[characters.NAME]+".txt", "w") as file:
        cfg.write(file)

def Playergetmoney():
    print("You have " + str(characters.PLAYER[characters.COINS]) + " coins")

def Playerinfo():

    print("Info:\n\tName: " + characters.PLAYER[characters.NAME] + "\n\tLanguage: " + characters.savelanguage + "\n\tCoins: " + str(characters.PLAYER[characters.COINS]) + "\n\tPlaytime: " + str((interim + characters.savetime)) + "\n\tHealth: " + str(characters.PLAYER[characters.HEALTH]) + "\n\n\n")

commands = {
    "help": game_help,
    "quit": lambda: exit("You commit suicide and leave this world."),
    "fight": fight,
    "rest": characters.game_rest_player,
    "forward": map.forward,
    "backwards": map.backwards,
    "right": map.right,
    "left": map.left,
    "save": save,
    "load": load,
    "money": Playergetmoney,
    "player": Playerinfo
}

dealercommands = {}



if __name__ == "__main__":
    characters.PLAYER[characters.NAME] = input("Enter your name: ")
    map.init(10, 10)
    print("Type help to list the available commands\n")
    while True:
        start = time.time()
        command = input("> ").lower().split(" ")[0]
        if command in commands:
            commands[command]()
            if characters.rest_counter == 1 or characters.rest_counter == 0:
                characters.rest_available = True
            elif command in ("left", "right", "forward", "backwards"):
                characters.rest_counter -= 1
        elif characters.rest_available == False:
            print(
                "You run around in circles and don't know what to do\nKeep moving to rest")
        else:
            print(
                "You run around in circles and don't know what to do")
        map.print_current_enemies()
        interim = interim + (time.time() - start)
