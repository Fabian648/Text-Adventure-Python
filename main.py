import os, sys, time

from ta_data.src.load_save import load
#from ta_data.src.modules import Logger, Backup

#Logger = Logger()


def game_load():
    command = input("Spiel laden oder neues spiel beginnen? >")
    new_commands = ["new", "New", "new game", "New game", "New Game"]
    load_commands = ["load", "Load", "load game", "Load game", "Load Game"]
    if command in new_commands:
        print("new")
        pass
    elif command in load_commands:
        load()
        pass
    else:
        game_load()





if __name__ == "__main__":
    game_load()
    print("end")
