import sys, regex as re, os
sys.path.append(".")

def show_saved_games():
    match = re.findall(r"([A-z]+\s?)*(?=_data)", str(os.listdir("Saved_Games")))
    for _ in match:
        match.remove('')
    return match

# load saved game
def load():

    for char_name in show_saved_games():
        print("Player " + char_name)

    namedata = input("Please enter the name of the saved character: ").lower()
    
    if namedata in show_saved_games():
        load_player(namedata)
    elif namedata == 'exit':
        return
    else:
        print("Not a valid option. Please chose one of the players or >exit<")

def load_player(name):
    
    pass