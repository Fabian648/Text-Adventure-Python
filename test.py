import configparser
import json, os
import configparser

#from ta_data.shops.shop import Shop
from ta_data.equipment.weapons import *

cfg = configparser.ConfigParser()
cfg.read(r"ta_data\META_data\shop_data\Weapons_data.ini")
item_list = [1,2]
def shopdata_generator():
    weapon_list=json.loads(cfg.get("WEAPONS", "WEAPONS_CLOSE_COMBAT"))
    for item in weapon_list:
        print(item)
        item_list.append(MeleeWeapon(name=item[0], damage=item[1], durability=item[2], max_durability=item[2], price=item[3]))

if 1 in item_list:
    print(1)