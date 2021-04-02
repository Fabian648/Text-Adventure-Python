import sys
sys.path.append(".")
from ta_data.equipment.weapons import MeleeWeapon

import mysql.connector
from ta_data.config import *
from ta_data.shops.shop import Shop


mydb = mysql.connector.connect(
    host=DB,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD
)

def read_database(ID, FIELD, KIND):
    mycursor = mydb.cursor()
    mycursor.execute("USE " + str(DB_NAME))
    mycursor.execute("SELECT " + FIELD + " FROM " + KIND )#+ " WHERE ID = " + str(ID))


    myresult = mycursor.fetchall()
    
    print(myresult)

#read_database("1", "*", "melee_weapons")

print("-"*100)


#mycursor = mydb.cursor()
#mycursor.execute("SELECT * FROM weapons WHERE ID = '%s'"% (str(id)))
#weapon_data = mycursor.fetchall()


print(MeleeWeapon(1))



#print(mycursor.execute("SELECT COUNT (*) FROM melee_weapons;"))
