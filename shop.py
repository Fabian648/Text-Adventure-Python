import random, os, json
from configparser import ConfigParser
import TA_Data.src.probability
import sys
from TA_Data.src.module_ta import Logger
pathtodir = os.getcwd()

Logger = Logger()
config = ConfigParser()
config.read('TA_Data\\game_data\\META_data\\shop_data\\Weapons_data.ini')

class Shop():

    def __init__(self, player, commands):
        self.player = player
        self.weapons_close_combat = json.loads(config.get('WEAPONS_CLOSE_COMBAT', 'WEAPONS_CLOSE_COMBAT'))
        self.weapons_ranged = json.loads(config.get("WEAPONS_RANGED", "WEAPONS_RANGED"))
        self.ammo = json.loads(config.get("AMMO", "AMMO"))
        self.available_items = []
        self.items = [self.weapons_close_combat, self.weapons_ranged, self.ammo]
        self.shop_item_id = {}
        self.commands = commands # {"buy": Shop.buy, "help": Shop.shop_help, "leave": Shop.shop_quit, "list items": Shop.shop_list_items}


    def shop(self):
        shop_commands = self.commands

        #os.system("cls")
        print("---- \nShop \n---- \nYour coins = " + self.player["money"] + "\n")

        
        
        self.shop_list_items()

        while True:
            command = input(": ").lower().split(" ")
            #print(type(command), len(command))
            if command[0] in shop_commands and command[0] == "buy":
                shop_commands[command[0]](self, command)
            elif command[0] in shop_commands:
                if shop_commands[command[0]](self) == "leave":
                    break
            else:
                print("Input is not a command enter help to list all available commands")
            
    def buy(self, command=None):
        command.pop(0)
        Shop.id_items(self)
        if command is not None and command != []:
            item_to_buy = []
            item_to_buy.append(" ".join(command).lower())
        else:
            item_to_buy = []
            item_to_buy.append(input("item to buy: ").lower())
        
        
        if item_to_buy[0] in self.shop_item_id:
            for item_groups in self.items:
                for item in item_groups:
                    if self.shop_item_id[item_to_buy[0].lower()] == item[1]:
                        item_to_buy.append(item[1])
                        item_to_buy.append(item[2])                 

                        validate = input("Are you sure you want to buy " + str(item_to_buy[0]) + " for " + str(item_to_buy[2]) + " coins? j/n : ").lower()
                        if validate == "j" and Shop.check_for_finaces(self, item_to_buy[2]):
                            
                            print(True)
                        else:
                            print("You canceld the purchase.")

        else:
            print("not an available item" + item_to_buy[0], self.shop_item_id)
    
    def shop_help(self):
        
        key_value = ""
        for i in self.commands:
            
            if type(i) == list:
                key_value = key_value + "-" + i[0] + ", "
            elif type(i) == str:
                try:
                    i = int(i)
                    pass
                except:
                    i = str(i)
                    key_value = key_value + "-" + i + "- "
            else:
                Logger.all_log("Error 3 in shop.py " + Logger.lineno())
                sys.exit("TypeError in shop.py")
        print(key_value)
    
    def shop_list_items(self):
        for item_group in self.items:
            for item in item_group:
                if item[0] != "Hand":
                    print(f"name: {item[0]:25} price: {item[2]:10}")
                    #  + {str(item[2]): 25}")
                    #print("name: " + item[0] + "\t \tprice: " + str(item[2]))

    def id_items(self):
        for item_group in self.items:
            for item in item_group:
                self.shop_item_id[item[0].lower()] = item[1]

    def check_for_finaces(self, itemcost):
        if float(self.player["money"]) >= float(itemcost):
            return True
        else:
            missing = float(itemcost) - float(self.player["money"])
            print("You are missing", missing, "coins to buy this item")
            return(False)

    def shop_quit(self):
        return "leave"


player = {'name': 'ben', 'money': '12.0', 'health': '200.0'}
commands = {"buy": Shop.buy, "help": Shop.shop_help, "leave": Shop.shop_quit, "list items": Shop.shop_list_items}

Shop(player=player,commands=commands).shop()