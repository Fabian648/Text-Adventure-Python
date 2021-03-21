import os, sys, time
from rich import print
from ta_data.src.character import load, new_player, save
from ta_data.players.player import *
from ta_data.src.TA_Errors import *
from ta_data.src.modules import Logger


def game_load():
    command = input("load game or new game?: ").lower().split(" ")
    new_commands = ["new", "neu"]
    load_commands = ["load", "laden"]
    # noch offen
    delete_commands = ["delete", "löschen", "loeschen"]
    if command[0] in new_commands:
        return new_player()
    elif command[0] in load_commands:
        return load()
    elif command[0] in delete_commands:
        try:
            print("delete not yet implemented")
            raise NotImplementedError("delete fuction not yet implemented")
        except NotImplementedError:
            return None
    else:
        print("command does not exsist")
        return game_load()
  
def list_base_commands(player):
    for key in commands_base:
        print("[blue]command", key)
    
def  list_player_commands(player):
    for key in commands_player:
        print('[blue]command', key)

def save_game(player):
    save(player)

def clear(player):
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def exit(player):
    save_game(player)
    sys.exit("proper shutdown")

commands_base = {
    'help': list_base_commands,
    'help player': list_player_commands,
    'save': save_game,
    'clear': clear,
    'exit': exit
        }

commands_player = {
    'list inventory': list_inventory,
    'player': list_player_stats
}


if __name__ == "__main__":
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    with open("versions/core-version.txt", "r")as file:
        core_version = file.readline().rstrip()
    with open("versions/db-version.txt", "r")as file:
        db_version = file.readline().rstrip()
    
    print("core version [bold red] " + core_version, "db version [bold red] " + db_version)
    player = None    

    try:
        while player == None:
            player = game_load()

        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")

        while True:
       
            command = input(">").lower()

            if command in commands_base:
                commands_base[command](player)
            elif command in commands_player:
                commands_player[command](player)
            else:
                print("command does not exsist")
                
    except KeyboardInterrupt:
        print("\nshutting down")
    except TA_Error as e:
        print("A text-adventure error has occured, check the logs if this error is persitant")
    
