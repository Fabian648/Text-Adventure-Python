import random
import map
import characters
from configparser import ConfigParser
import time
from pathlib import Path
import os

cfg = ConfigParser()

interim = 0


def game_help():
    print(commands.keys())


def load():

    namedata = input("Please enter the name: ")
    data = "Config_TA_" + namedata + ".txt"
    cfg.read(data)

    # Playerdaten
    characters.PLAYER[characters.NAME] = cfg.get("config_TA", "player")
    characters.savelanguage = cfg.get("config_TA", "language")
    characters.PLAYER[characters.COINS] = float(cfg.get("config_TA", "coins"))
    characters.savetime = float(cfg.get("config_TA", "time"))
    characters.PLAYER[characters.HEALTH] = float(cfg.get("config_TA", "HP"))

    # Skilldaten
    characters.PlayerFightEp = float(cfg.get("config_Skill", "AttackEP"))
    characters.fightlevel = int(cfg.get("config_Skill", "Attacklevel"))
    characters.skillfightlevel[characters.fightlevel] = True


def save():
    global interim
    # von Datei time rauslesen wenn sie exestiert

    tosavetime = interim + characters.savetime

    cfg["config_TA"] = {"Player": characters.PLAYER[characters.NAME],
                        "language": "en", "coins": characters.PLAYER[characters.COINS], "time": tosavetime, "HP": characters.PLAYER[characters.HEALTH]}
    cfg["config_Game"] = {}  # Rest Zeit usw. Map Größe
    cfg["config_Skill"] = {"Attacklevel": characters.fightlevel,
                           "AttackEP": characters.PlayerFightEp}  # Alles zu Skills

    with open("Config_TA_" + characters.PLAYER[characters.NAME]+".txt", "w") as file:
        cfg.write(file)


def Playergetmoney():
    print("You have " + str(characters.PLAYER[characters.COINS]) + " coins")


def Playerinfo():
    os.system("cls")
    time_all = interim + characters.savetime


    print("Info:\n\tName: " + characters.PLAYER[characters.NAME] + "\n\tLanguage: " + characters.savelanguage + "\n\tCoins: " + str(characters.PLAYER[characters.COINS]) + "\n\tStrength: " + str(characters.PLAYER[characters.STRENGTH]
                                                                                                                                                                                                  ) + "%\tLevel: " + str(characters.fightlevel) + "\n\tPlaytime: " + str(time_all) + "\n\tHealth: " + str(characters.PLAYER[characters.HEALTH]) + "\n\tFight Ep: " + str(characters.PlayerFightEp) + "\n\n\n")


def run():
    pass


commands = {
    "help": game_help,
    "quit": lambda: exit("You commit suicide and leave this world."),
    "rest": characters.game_rest_player,
    "forward": map.forward,
    "backwards": map.backwards,
    "right": map.right,
    "left": map.left,
    "save": save,
    "load": load,
    "money": Playergetmoney,
    "player": Playerinfo,
    "skill": characters.skills,
    "shop": characters.shop,
    "inv": characters.inv,
    "use": characters.use
}

dealercommands = {}


if __name__ == "__main__":
    characters.PLAYER[characters.NAME] = input("Enter your name: ")
    map.init(10, 10)
    print("Type help to list the available commands\n")
    while True:

        # Update Methoden
        characters.update()
        characters.skillsupdate()


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