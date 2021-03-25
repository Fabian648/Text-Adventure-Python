import sys, configparser, json, os, rich
from ta_data.src.modules import Logger
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
            item_list.append(MeleeWeapon(name=item[0], id=item[1], damage=item[2], durability=item[3], max_durability=item[4], price=item[5]))
        self.inventory["Melee Weapons"] = item_list

#base_shop = Shop(["melee"])
#for item in base_shop.inventory["Melee Weapons"]:
#    print(item.name)

def list_shop(player, shop, cmd):
    for key, value in shop.inventory.items():
        print("----------------------------------------", key, "----------------------------------------")
        rich.print(f"%-25s %-25s %-25s %-25s %-25s" % ("ID", "Name", "Damage", "Durability", "Price"))
        for item in value:
            #  print(key, item.price)
            rich.print(f"[bold green]%-25s [bold gray]%-25s [bold red]%-25s [bold #8B4513]%-25s [bold #FFD700]%-25s" % (item.id, item.name, item.damage, str(item.durability), item.price))

def buy_shop(player, shop, cmd):
    for key, value in shop.inventory.items():
        for item in value:
            if int(cmd) == item.id:
                if "y" in input("are you sure that you  want to buy " + item.name + " for " + str(item.price) + "coins? (y/n): ").lower():
                    if player.money >= item.price:
                        player.money -= item.price
                        player.weapon = item
                        print("Item was bought")
                    else:
                        print("Lacking money")
                break

def list_shop_commands(player, commands_shop, cmd):
    for key, value in commands_shop.items():
        print(key)

def shop_enter(player, commands_shop, shop_type=["melee"]):
    print("Welcome in the Shop!")
    print("You have " + str(player.money) + " coins.")
    try:
        while True:
            command = input("Shop >").lower().split(" ")
            Logger().eingabe_log(str(command), player.name)
            if len(command) == 1:
                command.append(None)
            if command[0] in commands_shop and command[0] != "exit":
                commands_shop[command[0]](player, shop=Shop(shop_type), cmd=command[1])
            elif command[0] == "exit" or command[0] == "leave":
                break
            else:
                print("command does not exsist")
    except Exception as e:
        Logger().error_log("an error has occured in shop", e)
        print("an error has ocured please check the logs")
