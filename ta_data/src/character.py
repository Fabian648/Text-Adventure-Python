import sys, regex as re, os, configparser, json, time
from unicodedata import name
sys.path.append(".")
from ta_data.equipment.weapons import MeleeWeapon
from ta_data.src.TA_Errors import FileLoadError, NoSavedGame
from ta_data.players.player import Player
from ta_data.src.modules import Logger
import mysql.connector
from ta_data.config import *

mydb = mysql.connector.connect(host=DB, port=DB_PORT, user=DB_USER, password=DB_PASSWORD)

def load(name=None):
    if name == None:
        name = input("Enter the playername that you want to load: ")
        if 'exit' in name or 'leave' in name:
            return None

    return load_player(name)

def load_player(famname, name):
    
    try:
        mycursor = mydb.cursor()
        mycursor.execute("USE TAUsers")
        mycursor.execute("SELECT * FROM UserDataDev WHERE Familyname = '%s' AND Name = '%s'" % (str(famname), str(name)))
        
        player_data = mycursor.fetchall()[0]
        print(player_data)
        player = Player(
            family_name=player_data[0], 
            name=player_data[2],
            money=player_data[3],
            max_health=player_data[4], 
            max_mana=player_data[5],
            health=player_data[6],
            mana=player_data[7],
            strength=player_data[8],
            weapon=MeleeWeapon(player_data[9])
            )

        return player

    except:
        print("no such save was found")
        return 
        
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
    mycursor = mydb.cursor()
    mycursor.execute("USE TAUsers")
    player = Player(name=player_name, max_health=200)
    sql = "INSERT INTO UserData (Name, Money, MaxHealth, MaxMana, Health, Mana, Strength, Weapon) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = [(player.name, player.money, player.max_health, player.max_mana, player.health, player.mana, player.strength, player.weapon.id)]
    mycursor.executemany(sql, val)
    mydb.commit()
    print("yaaaa")
    return player
    
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

def list_saved_players(famname):
    mycursor = mydb.cursor()
    mycursor.execute("USE TAUsers")
    mycursor.execute("SELECT Name FROM UserDataDev WHERE Familyname='" + famname + "'")
    player_names = mycursor.fetchall()
    playername_list = []
    for playername in player_names:
        print(" -" +str(playername[0]))
        playername_list.append(playername[0])
    return playername_list

def check_password(pass_hash):
    password = input("Please enter your Password: ")
    print(pass_hash, password)
    if pass_hash == password:
        return True
    else:
        print("the password was invalid")
        return False

def chose_player(player_list, familyname):
    command = str(input("Please enter a playername or create a new one: "))
    if 'exit' in command:
        return None
    elif command in player_list:
        return load_player(familyname, command)
    elif 'create' in command or 'new' in command:
        return create_player(player_list, familyname)
    else:
        print("Enterd value is not known")
        return chose_player(player_list, familyname)
    














