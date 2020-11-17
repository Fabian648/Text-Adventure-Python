import random
import map
import characters
from configparser import ConfigParser
import time
from pathlib import Path
import os
import sys

cfg = ConfigParser()
# Ist jetzt eine sehr unscchöne lösung die aber recht gut funktionieren sollte
global interim
interim = 0


def game_help():
    print(commands.keys())


# load saved game
def load():
    namedata = input("Please enter the name of the saved character: ")
    data = "Config_TA_" + namedata + ".txt"
    cfg.read(data)

    # check ob die file exsistiert
    if os.path.isfile(data):
        # hier werde (vllt?) ich ein backup der file erstellen lassen
        pass
    elif os.path.isfile(data) is False:
        # beendet den load vorgang und startet die eingabe erneut
        print("Dieser Speicherstand ist nicht vorhanden")
        # Lösung Problem Nr. 0
        eingabe()
    else:
        # diesen teil darf es auf keinen fall erreichen sonst ist bool weder True noch False
        # log wird noch eingebaut
        sys.exit("Crit Problem in load siehe log")

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
    print("Speicherstand " + namedata + " erfolgreich geladen")
    # Lösung Problem Nr. 0
    eingabe()


# save pending game
def save():
    # noch ohne backup
    global interim
    # von Datei time rauslesen wenn sie exestiert
    # Frage: ist das die Spieldauer Zeit oder welche Zeit ist dies?
    # Frage wenn Datei schon vorhanden, sollen wir dann fragen ob diese überschrieben werden soll?
    # oder gleich ein backup erstellen und Frage lassen? - dann würde ich kein backup beim laden des spieles machen

    tosavetime = interim + characters.savetime

    cfg["config_TA"] = {"Player": characters.PLAYER[characters.NAME],
                        "language": "en",
                        "coins": characters.PLAYER[characters.COINS],
                        "time": tosavetime,
                        "HP": characters.PLAYER[characters.HEALTH]}
    cfg["config_Game"] = {}  # Rest Zeit usw. Map Größe
    cfg["config_Skill"] = {"Attacklevel": characters.fightlevel,
                           "AttackEP": characters.PlayerFightEp}  # Alles zu Skills

    with open("Config_TA_" + characters.PLAYER[characters.NAME] + ".txt", "w") as file:
        cfg.write(file)


def player_get_money():
    print("You have " + str(characters.PLAYER[characters.COINS]) + " coins")


def player_info():
    os.system("cls")
    time_all = interim + characters.savetime

    print("Info:\n\tName: " + characters.PLAYER[characters.NAME],
          "\n\tLanguage: " + characters.savelanguage,
          "\n\tCoins: " + str(characters.PLAYER[characters.COINS]),
          "\n\tStrength: " + str(characters.PLAYER[characters.STRENGTH]),
          "%\tLevel: " + str(characters.fightlevel),
          "\n\tPlaytime: " + str(time_all),
          "\n\tHealth: " + str(characters.PLAYER[characters.HEALTH]),
          "\n\tFight Ep: " + str(characters.PlayerFightEp),
          "\n\n\n")


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
    "money": player_get_money,
    "player": player_info,
    "skill": characters.skills,
    "shop": characters.shop,
    "inv": characters.inv,
    "use": characters.use
}

dealercommands = {}


def eingabe():
    global interim
    # Update Methoden
    characters.update()
    characters.skillsupdate()

    start = time.time()
    command = input("> ").lower().split(" ")[0]
    # Problem Nr. 0
    # hier wird der Spieler automatisch auch nach jeder unrelevanten eingabe auch load save etc. in die nächste aktion
    # gesetzt ist das gewollt?
    if command in commands:
        commands[command]()
        if characters.rest_counter == 1 or characters.rest_counter == 0:
            characters.rest_available = True
        elif command in ("left", "right", "forward", "backwards"):
            characters.rest_counter -= 1

    elif not characters.rest_available:
        print(
            "You run around in circles and don't know what to do\nKeep moving to rest")
    else:
        print(
            "You run around in circles and don't know what to do")
    map.print_current_enemies()
    interim = interim + (time.time() - start)


if __name__ == "__main__":

    characters.PLAYER[characters.NAME] = input("Enter your name: ")
    map.init(10, 10)
    print("Type -help- to list the available commands\n")
    while True:
        eingabe()

