import os, sys, time

from ta_data.src.character import load, new_player, save
from ta_data.src.TA_Errors import InvalidStats
from ta_data.src.modules import Logger





def game_load():
    command = input("Spiel laden oder neues spiel beginnen: ")
    new_commands = ["new", "New", "new game", "New game", "New Game"]
    load_commands = ["load", "Load", "load game", "Load game", "Load Game"]
    if command in new_commands:
        return new_player()
    elif command in load_commands:
        return load()
    else:
        return game_load()

  
def list_commands(player):
    for key in commands:
        print("command", key)
    
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

commands = {
        'help': list_commands,
        'save': save_game,
        'clear': clear,
        'exit': exit
        }


if __name__ == "__main__":
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    
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
            if command in commands:
                commands[command](player)
            else:
                print("command does not exsist")
    except KeyboardInterrupt:
        print("\nshutting down")
    except TA_Error as e:
        print("A text-adventure error has occured, check the logs if this error is persitant")
    
