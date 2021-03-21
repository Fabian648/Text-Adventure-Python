import sys, regex as re, os, configparser
sys.path.append(".")
from ta_data.players.player import Player

def show_saved_games():
    match = re.findall(r"(\w+\s?)*(?=_data)", str(os.listdir("Saved_Games")))
    for _ in match:
        match.remove('')
    return match

def load():

    for char_name in show_saved_games():
        print("Player " + char_name)

    namedata = input("Please enter the name of the saved character: ").lower()
    
    if namedata in show_saved_games():
        return load_player(namedata)
    elif namedata == 'exit':
        return None
    else:
        print("Not a valid option. Please chose one of the players or >exit<")
        load()

def load_player(name):
    cfg = configparser.ConfigParser()
    if os.path.isfile(os.path.join("Saved_Games", name + "_data", "Config_TA_" + name + ".ini")):
        cfg.read(os.path.join("Saved_Games", name + "_data", "Config_TA_" + name + ".ini"))
    return Player(name=cfg.get("config_TA", "name"), max_health=cfg.get("config_TA", "max_health"), health=cfg.get("config_TA", "health"))

def new_player():
    player_name = input("Please enter a player name: ").lower()
    if player_name == "list":
        for char_name in show_saved_games():
            print("Player name " + char_name)
        new_player()
    elif player_name == "exit":
        return None
    elif player_name not in show_saved_games():
        return create_player(player_name)
    else:
        print("player name allready taken, type list to list all taken names")
        new_player()

def create_player(player_name):
    return Player(name=player_name, max_health=200)
    
def save(player):
    if not os.path.isfile(os.path.join("Saved_Games", player.name + "_data", "Config_TA_" + player.name + ".ini")):
        os.makedirs(os.path.join("Saved_Games", player.name + "_data"))

    with open(os.path.join("Saved_Games", player.name + "_data", "Config_TA_" + player.name + ".ini"), "w") as file:
        file.write("[config_TA]")
        file.write("\nname=" + str(player.name))
        file.write("\nmax_health=" + str(player.max_health))
        file.write("\nhealth=" + str(player.health))
    
    print("game saved")






















