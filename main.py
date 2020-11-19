import map
import characters
from configparser import ConfigParser
import time
import os
import sys
import regex as re
from Backup_py import Logger
from Backup_py import Backup as Backup

Logger = Logger()
cfg = ConfigParser()
# Ist jetzt eine sehr unscchöne lösung die aber recht gut funktionieren sollte
global interim
interim = 0
print(os.getcwd())


# save location
def saved_file_loc(name=characters.PLAYER[characters.NAME]):
    if name == "" or name is None:
        name = characters.PLAYER[characters.NAME]
    else:
        pass
    save_file_name = os.path.join("Saved_Games", "Config_TA_" + name + ".ini")
    Logger.all_log("Name of folder and save " + save_file_name + Logger.lineno())
    return save_file_name


def game_help():
    key_value = ""
    for i in commands.keys():
        key_value = key_value + " -" + i + "- "
    print(key_value)
    eingabe()


# load saved game
def load(extra=False):
    namedata = input("Please enter the name of the saved character: ")
    data = saved_file_loc(namedata)
    cfg.read(data)

    # check ob die file exsistiert
    if os.path.isfile(data):
        # hier werde (vllt?) ich ein backup der file erstellen lassen
        pass
    elif os.path.isfile(data) is False:
        # beendet den load vorgang und startet die eingabe erneut
        print("Dieser Speicherstand ist nicht vorhanden")
        if extra:
            game_load()
            return
        else:
            # Lösung Problem Nr. 0
            eingabe()
            return
    else:
        # diesen teil darf es auf keinen fall erreichen sonst ist bool weder True noch False
        Logger.all_log("Fehler 0 in main.py" + Logger.lineno())
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
def save(extra=None):
    global interim

    # von Datei time rauslesen wenn sie existiert
    # Überprüfung ob der Speicherstan vorhanden ist

    save_file = saved_file_loc(characters.PLAYER[characters.NAME])
    if os.path.isfile(save_file):
        ueberschrieben = input("Spielstand Überschreiben? (J/N): ")

        if ueberschrieben == "J" or ueberschrieben == "j":
            Backup(save_file)
        elif ueberschrieben == "N" or ueberschrieben == "n":
            print("Saving canceled")
            eingabe()
        else:
            print("Unknown Input")
            save()
    else:
        Logger.all_log("Dir muss erst erstellt werden" + Logger.lineno())

    print("Game is Saving")
    tosavetime = interim + characters.savetime

    cfg["config_TA"] = {"Player": characters.PLAYER[characters.NAME],
                        "language": "en",
                        "coins": characters.PLAYER[characters.COINS],
                        "time": tosavetime,
                        "HP": characters.PLAYER[characters.HEALTH]}
    cfg["config_Game"] = {}  # Rest Zeit usw. Map Größe
    cfg["config_Skill"] = {"Attacklevel": characters.fightlevel,
                           "AttackEP": characters.PlayerFightEp}  # Alles zu Skills

    with open(saved_file_loc(), "w") as file:
        cfg.write(file)

    Logger.all_log("Pending game saved" + Logger.lineno())

    if extra == "end":
        sys.exit("Byby")
    elif extra is None:
        eingabe()
    else:
        Logger.all_log("passed argument to save is not known")
        pass


def player_get_money():
    print("You have " + str(characters.PLAYER[characters.COINS]) + " coins")
    eingabe()


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
    eingabe()


def run():
    pass


commands = {
    "help": game_help,
    "quit": lambda: exit("You commit suicide and leave this world."),
    "end": lambda: exit(save("end")),
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
    # Übermittelt die eeingabe und den Namen des characters
    Logger.eingabe_log(command, characters.PLAYER[characters.NAME])

    if command in commands:
        commands[command]()
        if characters.rest_counter == 1 or characters.rest_counter == 0:
            characters.rest_available = True
        elif command in ("left", "right", "forward", "backwards"):
            # verhindert das spammen von rest
            characters.rest_counter -= 1

    elif not characters.rest_available:
        print(
            "You run around in circles and don't know what to do\nKeep moving to rest"
        )
    else:
        print("This command doesn't exsist")
        eingabe()

    map.print_current_enemies()
    interim = interim + (time.time() - start)


def game_load():
    first = input("new game or load game? : ")
    new_game = ["new", "New", "new game", "New game", "New Game"]
    load_game = ["load", "Load", "load game", "Load game", "Load Game"]
    if first in new_game:
        buffer = input("Enter your name: ")
        # liste mit nicht gültigen namen - exsistieren schon oder ist leer -> ""
        # #dies können wir auch beleibig erweitern
        buffer_not = re.findall(r"(?<=Config_TA_)([A-z]+\s?)*(?=\.ini)", str(os.listdir("Saved_Games")))
        # hier können wir Bestimmte eingaben verhindern
        buffer_not_valid = ["", " ", "Bennexy"]
        if buffer not in buffer_not and buffer not in buffer_not_valid:
            characters.PLAYER[characters.NAME] = buffer
        elif buffer in buffer_not:
            print("Name is allready taken")
            game_load()
        elif buffer in buffer_not_valid:
            print("Name is not Valid")
            game_load()
        else:
            Logger.log("Fehler 0 in main.py" + Logger.lineno())
            sys.exit("Crit Problem in game_load siehe log")

        print("Player Charakter " + characters.PLAYER[characters.NAME] + " made")
        pass
    elif first in load_game:
        load(True)
        pass
    else:
        print("Command not found")
        game_load()


if __name__ == "__main__":

    game_load()
    # print(type(characters.PLAYER[characters.NAME]), characters.PLAYER[characters.NAME])
    map.init(10, 10)
    print("Type -help- to list the available commands\n")
    while True:
        eingabe()
