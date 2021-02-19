"""This file manages the main process

This file contains following functions:
    saved_file_loc - checks if the char has a save
    game_help - prints the game commands
    load - loads a saved game
    save - saves the pending game
    player_get_money - prints the money amount available
    player_info - prints the chars stats
    run - notyetimplemented
    eingabe - füührt befehle aus
    game_load - erste funktion erstellt neues spiel oder lädt ein vorhandenes
    quiter - quits game sesion
    end - ends the game and saves it

"""
# from game_data import map
# from game_data.Shops import shop, dealer_shop, ammo_shop

# Externe imports
import os
import time
import sys
from TA_Data.src.TA_Errors import ModuleNotFoundError, NotImplementedError
try:
    from configparser import ConfigParser   
    import regex as re
except:
    raise ModuleNotFoundError()
    

# interne imports
import characters
import map

from TA_Data.src.module_ta import Backup
from TA_Data.src.module_ta import Logger

Logger = Logger()
cfg = ConfigParser()
cfgmap = ConfigParser()
# Ist jetzt eine sehr unscchöne lösung die aber recht gut funktionieren sollte
global interim
interim = 0


# save location
def saved_file_loc(data="name", name=characters.PLAYER[characters.NAME]):
    if name == "" or name is None:
        name = characters.PLAYER[characters.NAME]
    else:
        pass
    if data == "name":
        save_file_name = os.path.join("Saved_Games", name + "_data", "Config_TA_" + name + ".ini")
    elif data == "map":
        save_file_name = os.path.join("Saved_Games", name + "_data", "map_" + name + ".ini")
    else:
        saved_file_loc("name", name)
    Logger.all_log("Name of folder and save " + save_file_name + Logger.lineno())
    return save_file_name


def game_help():
    key_value = ""
    for i in commands.keys():
        
        if type(i) == list:
            key_value = key_value + "-" + i[0] + ", "
        elif type(i) == str:
            try:
                i = int(i)
                pass
            except:
                i = str(i)
                key_value = key_value + "-" + i + "- "
        else:
            Logger.all_log("Error 3 in main.py " + Logger.lineno())
            sys.exit("TypeError in main.py")
    print(key_value)
    eingabe()


# load saved game
def load(extra=None):
    if extra is not None:
        namedata = extra
        extra = None
    else:
        namedata = input("Please enter the name of the saved character: ").lower()
    if namedata == "help":
        match = re.findall(r"([A-z]+\s?)*(?=_data)", str(os.listdir("Saved_Games")))
        metch = []
        x = int(len(match) / 2)
        for i in range(x):
            metch.append('')
        match = list(set(match) - set(metch))
        print("Saved games are " + str(match))
        load()

    data = saved_file_loc("name", namedata)
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
        Logger.all_log("Error 2 in main.py" + Logger.lineno())
        sys.exit("Process finished with Error code 2 in main.py/load siehe log")

    # Playerdaten
    characters.PLAYER[characters.NAME] = cfg.get("config_TA", "player")
    characters.savelanguage = cfg.get("config_TA", "language")
    characters.PLAYER[characters.COINS] = float(cfg.get("config_TA", "coins"))
    characters.savetime = float(cfg.get("config_TA", "time"))
    characters.PLAYER[characters.HEALTH] = float(cfg.get("config_TA", "HP"))
    player = {}
    player["name"] = cfg.get("config_TA", "player")
    player["money"] = cfg.get("config_TA", "coins")
    player["health"] = cfg.get("config_TA", "hp")
    """print(player)"""
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

    save_file = saved_file_loc()
    save_file_map = saved_file_loc("map")
    if os.path.isfile(save_file):
        ueberschrieben = input("Spielstand Überschreiben? (J/N): ")

        if ueberschrieben == "J" or ueberschrieben == "j":
            Backup(save_file)
            Backup(save_file_map)
        elif ueberschrieben == "N" or ueberschrieben == "n" and extra is None:
            print("Saving canceled")
            eingabe()
        elif ueberschrieben == "N" or ueberschrieben == "n" and extra is not None:
            sys.exit("By")
        else:
            print("Unknown Input")
            if extra is None:
                save()
            else:
                save(extra)
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

    cfgmap["mapdata"] = {"mapdata": "test"}
    
    with open(saved_file_loc("map"), "w") as file:
        cfgmap.write(file)

    Logger.all_log("Pending game saved" + Logger.lineno())

    if extra == "end":
        Logger.all_log("Exit code 0" + Logger.lineno())
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
    raise NotImplementedError("in main function run")


def eingabe():
    global interim
    # Update Methoden
    characters.update()
    characters.skillsupdate()

    start = time.time()
    if characters.PLAYER[characters.NAME] == "" or characters.PLAYER[characters.NAME] == " ":
        game_load()
    else:
        pass
    command = input("> ").lower().split(" ")[0]
    # Übermittelt die eeingabe und den Namen des characters
    Logger.eingabe_log(command, characters.PLAYER[characters.NAME])
    if command in commands:
        commands[command]()
        if characters.rest_counter == 1 or characters.rest_counter == 0:
            characters.rest_available = True
        elif command in [commands]:
            # verhindert das spammen von rest
            characters.rest_counter -= 1
            print("moin")
        else:    
            print("This command doesn't exsist")
            eingabe()

    map.print_current_enemies()
    interim = interim + (time.time() - start)


def game_load():
    first = input("new game or load game? : ").lower().split(" ")
    new_game = ["new", "New", "new game", "New game", "New Game"]
    load_game = ["load", "Load", "load game", "Load game", "Load Game"]
    if first[0] in new_game:
        buffer = input("Enter your name: ").lower()
        # liste mit nicht gültigen namen - exsistieren schon oder ist leer -> ""
        # #dies können wir auch beleibig erweitern
        buffer_not = re.findall(r"(?<=Config_TA_)(\w+\s?)*(?=\.ini)", str(os.listdir("Saved_Games")))
        # hier können wir Bestimmte eingaben verhindern
        buffer_not_valid = ["", " ", "bennexy", "help"]
        # print(buffer, buffer_not)

        # hier überprüfen wir ob der name schon vergeben ist
        if buffer not in buffer_not and buffer not in buffer_not_valid:
            characters.PLAYER[characters.NAME] = buffer
        elif buffer == "help":
            print("The names " + str(buffer_not) + " are allready taken")
            print("The names " + str(buffer_not_valid) + " are not Valid")
            game_load()
        elif buffer in buffer_not:
            print("Name is allready taken")
            game_load()
        elif buffer in buffer_not_valid:
            print("Name is not Valid")
            game_load()
        else:
            Logger.all_log("Error 2 in main.py" + Logger.lineno())
            sys.exit("Process finished with error code 2 main.py/game_load siehe log")

        print("Player Charakter " + characters.PLAYER[characters.NAME] + " made")
        pass
    elif first[0] in load_game:
        
        if len(first) != 1:
            extra = first[1]
        else:
            extra = None
        load(extra)
    else:
        print("Command not found")
        game_load()


def quiter():
    Logger.all_log("Exit code 2" + Logger.lineno()) + sys.exit(print("You commit suicide and leave this world."))


def ender():
    exit(save("end"))


commands = {
    "help" : game_help,
    "quit" : quiter,
    "end" : ender,
    "rest" : characters.game_rest_player,
    "forward" : map.forward,
    "back" : map.backwards,
    "right" : map.right,
    "left" : map.left,
    "5" : characters.game_rest_player,
    "8" : map.forward,
    "2" : map.backwards,
    "6" : map.right,
    "4" : map.left,
    "save" : save,
    "load" : load,
    "coins" : player_get_money,
    "player" : player_info,
    "skill" : characters.skills,
    "shop" : characters.shop, # pass player
    "inv" : characters.inv,
    "use" : characters.invenv_use
}

dealercommands = {}


if __name__ == "__main__":

    map.init(10, 10)
    print("Type -help- to list the available commands, works in modules to")
    game_load()
    # print(type(characters.PLAYER[characters.NAME]), characters.PLAYER[characters.NAME])

    while True:
        eingabe()
