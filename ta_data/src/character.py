import sys, regex as re, os, configparser, json, time
sys.path.append(".")
from ta_data.equipment.weapons import MeleeWeapon
from ta_data.src.TA_Errors import FileLoadError, NoSavedGame
from ta_data.players.player import Player
from ta_data.src.modules import Logger
import mysql.connector
from ta_data.config import *

mydb = mysql.connector.connect(host=DB, port=DB_PORT, user=DB_USER, password=DB_PASSWORD)

def show_saved_games():
    try:
        match = re.findall(r"(\w+\s?)*(?=_data)", str(os.listdir("Saved_Games")))
        for _ in match:
            match.remove('')
        return match
    except FileNotFoundError:
        print("No Games saved")
        return []

def load(name=None):
    if name == None:
        if show_saved_games() == []:
            print("No save found, please create a new one.")
            return new_player()
        else:
            for char_name in show_saved_games():
                print("Player " + char_name)

        namedata = input("Please enter the name of the saved character: ").lower()
        
        if namedata in show_saved_games():
            return load_player(namedata)
        elif namedata == 'exit':
            return None
        else:
            print("Not a valid option. Please chose one of the players or >exit<")
            return load()
    else:
        print(load_player(name))
        return load_player(name)

def load_player(name):
    cfg = configparser.ConfigParser()
    if os.path.isfile(os.path.join("Saved_Games", name + "_data", "Config_TA_" + name + ".ini")):
        cfg.read(os.path.join("Saved_Games", name + "_data", "Config_TA_" + name + ".ini"))
    else:
        try:
            raise NoSavedGame("The save for the player " + name + " was not found")
        except NoSavedGame:
            print("No save with the player name " + name + " was found.")
            return None
    try:
        mycursor = mydb.cursor()
        mycursor.execute("USE TAUsers")
        mycursor.execute("SELECT * FROM UserData WHERE Name = '%s'" % str(name))
        
        player_data = mycursor.fetchall()[0]
        print(player_data[7])

        return Player(
            name=player_data[0], 
            money=player_data[1],
            max_health=player_data[2], 
            max_mana=player_data[3],
            health=player_data[4],
            mana=player_data[5],
            strength=player_data[6],
            weapon=MeleeWeapon(player_data[7])
            )

    except json.decoder.JSONDecodeError:
        try:
            raise FileLoadError("error loading " + str(os.path.join("Saved_Games", name + "_data", "Config_TA_" + name + ".ini")))
        except FileLoadError:
            print("There was a Error Loading the Requested save.")
            return None
        
def new_player():
    player_name = input("Please enter a player name: ").lower()
    if player_name == "list":
        for char_name in show_saved_games():
            print("Player name " + char_name)
        return new_player()
    elif player_name == "exit":
        return None
    elif player_name not in show_saved_games():
        return create_player(player_name)
    else:
        print("player name allready taken, type list to list all taken names")
        return new_player()

def create_player(player_name):
    return Player(name=player_name, max_health=200)
    
def save(player):
    
    """if not os.path.isfile(os.path.join("Saved_Games", player.name + "_data", "Config_TA_" + player.name + ".ini")):
        os.makedirs(os.path.join("Saved_Games", player.name + "_data"))

    with open(os.path.join("Saved_Games", player.name + "_data", "Config_TA_" + player.name + ".ini"), "w") as file:
        file.write("[config_TA]")
        file.write("\nname=" + str(player.name))
        file.write("\nmax_health=" + str(player.max_health))
        file.write("\nhealth=" + str(player.health))
        file.write("\nmax_mana=" + str(player.max_mana))
        file.write("\nmana=" + str(player.mana))
        file.write("\nmoney=" + str(player.money))
        file.write("\nskills=" + json.dumps(player.skills))
        file.write("\nstrength=" + str(player.strength))
        file.write("\nweapon=" + json.dumps(player.weapon.__dict__))

        file.write("\n\n[Inventory]")
        file.write("\nbackpack=" + json.dumps(player.inventory))
        """
    mycursor = mydb.cursor()
    mycursor.execute("USE TAUsers")

    mycursor.execute(f"UPDATE UserData SET MaxHealth = '%s' WHERE Name = '%s'" %(player.max_health, player.name))
    mycursor.execute(f"UPDATE UserData SET MaxMana = '%s' WHERE Name = '%s'" %(player.max_mana, player.name))
    mycursor.execute(f"UPDATE UserData SET Health = '%s' WHERE Name = '%s'" %(player.health, player.name))
    mycursor.execute(f"UPDATE UserData SET Mana = '%s' WHERE Name = '%s'" %(player.mana, player.name))
    mycursor.execute(f"UPDATE UserData SET Health = '%s' WHERE Name = '%s'" %(player.health, player.name))
    mycursor.execute(f"UPDATE UserData SET Money = '%s' WHERE Name = '%s'" %(player.money, player.name))
    mycursor.execute(f"UPDATE UserData SET Weapon = '%s' WHERE Name = '%s'" %(player.weapon.id, player.name))
    mycursor.execute(f"UPDATE UserData SET Strength = '%s' WHERE Name = '%s'" %(player.strength, player.name))

    mydb.commit()
    #sql = "INSERT INTO UserData (Name, Money, MaxHealth, MaxHealth, Health, Mana, Strength, Weapon) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    #val = [(player.name, player.money, player.max_health, player.max_mana, player.health, player.mana, player.strength, player.weapon.id)]

    print("game saved")






















