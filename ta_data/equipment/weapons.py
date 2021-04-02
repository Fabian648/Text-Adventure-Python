import sys
sys.path.append(".")
import mysql.connector
from ta_data.config import *

mydb = mysql.connector.connect(host=DB, port=DB_PORT, user=DB_USER, password=DB_PASSWORD)
mycursor = mydb.cursor()
mycursor.execute("USE " + str(DB_NAME))

class Weapon:
    def __init__(self, id, weapon_data):
        
        self.id = weapon_data[0]
        self.name = weapon_data[1]
        self.damage = weapon_data[2]
        self.accuracy = weapon_data[3]
        self.price = weapon_data[4]
        self.range = weapon_data[5]
        self.durability = weapon_data[6]
        self.max_durability = weapon_data[7]
        #print(self.id, self.name, self.damage, self.accuracy, self.price, self.range, self.durability, self.max_durability)
        
        

class MeleeWeapon(Weapon):
    def __init__(self, id):
        mycursor.execute("SELECT * FROM weapons WHERE ID = '%s'"% (str(id)))
        weapon_data = mycursor.fetchall()[0]
        super().__init__(id=id, weapon_data=weapon_data)


class RangedWeapon(Weapon):
    def __init__(self, id):
        mycursor.execute("SELECT * FROM weapons WHERE ID = " + str(id))
        weapon_data = mycursor.fetchall()[0]
        super().__init__(id=id, weapon_data=weapon_data)

