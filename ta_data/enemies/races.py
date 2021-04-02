import sys
sys.path.append(".")

from ta_data.equipment.weapons import MeleeWeapon
from ta_data.creature import Creature 
import mysql.connector
from ta_data.config import *

mydb = mysql.connector.connect(host=DB, port=DB_PORT, user=DB_USER, password=DB_PASSWORD)
mycursor = mydb.cursor()
mycursor.execute("USE Enemies")



class Human(Creature):

    def __init__(self, id=1):
        mycursor.execute("SELECT * FROM Human WHERE ID = '%s'" % id)
        enemy_data = mycursor.fetchall()[0]
        super().__init__(
            name=enemy_data[1], 
            money=enemy_data[2],
            max_health=enemy_data[3], 
            max_mana=enemy_data[4],
            health=enemy_data[5], 
            mana=enemy_data[6], 
            strength=enemy_data[7],
            weapon=MeleeWeapon(enemy_data[8])
            )
         

class Ork(Creature):

    def __init__(self, id):
        pass

class Elf(Creature):

    def __init__(self, id):
        pass