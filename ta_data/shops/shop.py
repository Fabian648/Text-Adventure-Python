import sys, configparser, json, os, rich
sys.path.append(".")
from ta_data.equipment.weapons import *
cfg = configparser.ConfigParser()
cfg.read(os.path.join("ta_data", "META_data", "shop_data", "Weapons_data.ini"))

class Shop:
    def __init__(self, shop_type=None):
        self.inventory = {}
        if "melee" in shop_type:
            self.load_inventory_melee()
        
    
    def load_inventory_melee(self):
        weapon_list=json.loads(cfg.get("WEAPONS", "WEAPONS_CLOSE_COMBAT"))
        item_list = []
        for item in weapon_list:
            #print(item)
            item_list.append(MeleeWeapon(name=item[0], damage=item[1], durability=item[2], max_durability=item[2], price=item[3]))
        self.inventory["Melee Weapons"] = item_list

#base_shop = Shop(["melee"])
#for item in base_shop.inventory["Melee Weapons"]:
#    print(item.name)

def list_shop(player, shop, cmd):
    for key, value in shop.inventory.items():
        print("----------------------------------------", key, "----------------------------------------")
        rich.print(f"%-25s %-25s %-25s %-25s" % ("Name", "Damage", "Durability", "Price"))
        for item in value:
            #  print(key, item.price)
            rich.print(f"[bold gray]%-25s [bold red]%-25s [bold #8B4513]%-25s [bold #FFD700]%-25s" % (item.name, item.damage, str(item.durability), item.price))

def buy_shop(player, shop, cmd):
    cmd[0] = ""
    item_to_buy = ""
    for element in cmd:
        item_to_buy += element
    print(item_to_buy)
    itemnames = []
    for key, value in shop.inventory.items():
        for item in value:
            itemnames.append([key, item.name.replace(" ", "").lower(), item.price, item])

    def buy(itemnames, player):
        for item in itemnames:
            if item_to_buy == item[1]:
                if "y" in input("Are you sure that you want to buy " + str(item[0]) + " " + str(item[1]) + " for " + str(item[2]) + " coins? (y/n): ").lower():
                    if player.money - item[2] >= 0:
                        player.money -= item[2]
                        player.inventory[item[1]] = item[3]
                    else:
                        print("Couldn't buy item " + str(item[1]), "not enough money.")
    



def shop_enter(player, commands_shop, shop_type=["melee"]):
    print("Welcome in the Shop!")
    while True:
        command = input("Shop >").lower().split(" ")
        if command[0] in commands_shop and command[0] != "exit":
            commands_shop[command[0]](player, shop=Shop(shop_type), cmd=command)
        elif command == "exit" or command == "leave":
            break
        else:
            print("command does not exsist")
