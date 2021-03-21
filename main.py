import os, sys, time

from ta_data.src.character import load, new_player, save
#from ta_data.src.modules import Logger, Backup

#Logger = Logger()




def game_load():
    command = input("Spiel laden oder neues spiel beginnen:")
    new_commands = ["new", "New", "new game", "New game", "New Game"]
    load_commands = ["load", "Load", "load game", "Load game", "Load Game"]
    if command in new_commands:
        return new_player()
    elif command in load_commands:
        return load()
    else:
        game_load()


    

    
    
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
    
commands = {
        'help': list_commands,
        'save': save_game,
        'clear': clear
        }


if __name__ == "__main__":
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
        

    try:
        player = None
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
    
