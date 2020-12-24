import random, os
from configparser import ConfigParser
pathtodir = os.getcwd()
import characters
import TA_Data.src.probability
import sys
from TA_Data.src.module_ta import Logger

Logger = Logger()
config = Configparser()
config.

class Shop():

    def __init__(self):
        self.player = 
    

    def entry(self):

        os.system("cls")
        running_shop_loop = True
        print("Shop \nYour coins = " + str(PLAYER[5]))

        for i in WEAPONS:
            if i[NAME] != "hand":
                print(i[NAME] + "\tprice: " + str(i[PRICE]))

        while running_shop_loop:

            shop_command = input(": ").lower()

            if shop_command in shop_commands:
                running_shop_loop = shop_commands[shop_command]()

                if running_shop_loop:
                    True

                elif not running_shop_loop:
                    print("You Leave the shop")

                else:
                    Logger.all_log("Error code 2 in shop.py" + Logger.lineno())
                    sys.exit("Exit code 3")

            else:
                print("this command is invalid. Type -help- to see the shop commands. ")

