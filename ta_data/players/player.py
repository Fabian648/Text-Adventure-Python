import sys
sys.path.append(".")

from ta_data.character import Character

class Player(Character):

    def __init__(self):
        super().__init__()
        