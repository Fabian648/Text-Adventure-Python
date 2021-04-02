import sys, json, os
sys.path.append(".")
from rich import print
from ta_data.src.modules import Logger
from ta_data.equipment.weapons import *
from ta_data.config import *
import mysql.connector

mydb = mysql.connector.connect(host=DB, port=DB_PORT, user=DB_USER, password=DB_PASSWORD)


class Shop:
    def __init__(self, shop_type=None):
        self.inventory = {}
        if "melee" in shop_type:
            self.load_inventory_melee()
        
    
    def load_inventory_melee(self):
        mycursor = mydb.cursor()
        mycursor.execute("USE " + str(DB_NAME))
        mycursor.execute("SELECT * FROM weapons" )
        weapons_list = mycursor.fetchall()
        item_list = []
        for weapon in weapons_list:
            item_list.append(MeleeWeapon(id = weapon[0]))
        self.inventory['melee'] = item_list

        

#base_shop = Shop(["melee"])
#for item in base_shop.inventory["Melee Weapons"]:
#    print(item.name)

def list_shop(player, shop):
    for key, value in shop.inventory.items():
        print("|---------------------------------------------|", key, "|---------------------------------------------|")
        print(f"%-25s %-25s %-25s %-25s %-25s %-25s %-25s" % ("ID", "Name", "Damage", "Durability", "hitchance in %", "Price", "range"))
        for item in value:
            #  print(key, item.price)
            print(f"[bold green]%-25s [bold gray]%-25s [bold red]%-25s [bold #8B4513]%-25s [bold blue]%-25s [bold #FFD700]%-25s [bold white]%-25s" % (item.id, item.name, item.damage, str(item.durability), item.accuracy, item.price, item.range))

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

def list_shop_commands(player, commands_shop):
    for key in commands_shop:
        print("[blue]command",key)
    print("[blue]command", "exit")

def shop_enter(player, commands_shop, shop_type=["melee"]):
    print("Welcome in the Shop!")
    print("You have " + str(player.money) + " coins.")
    shop=Shop(shop_type)
    try:
        while True:
            command = input("Shop >").lower().split(" ")
            Logger().eingabe_log(str(command), player.name)
            if command[0] == 'buy':
                commands_shop[command[0]](player, shop=shop, cmd=command[1])
            elif command[0] == "help":
                commands_shop[command[0]](player, commands_shop)
            elif command[0] == "exit" or command[0] == "leave":
                break
            elif command[0] in commands_shop:
                commands_shop[command[0]](player, shop=shop)
            else:
                print("command does not exsist")
    except Exception as e:
        Logger().error_log("an error has occured in shop", e)
        print("an error has ocured please check the logs")
