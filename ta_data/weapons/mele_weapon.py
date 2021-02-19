import sys
sys.path.append(".")

from ta_data.weapons.weapon import Weapon

class MeleWeapon(Weapon):

    def __init__(self):
        super().__init__()