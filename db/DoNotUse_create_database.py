import sys
sys.path.append(".")
import mysql.connector
from ta_data.config import *
from ta_data.src.character import load_player

mydb = mysql.connector.connect(
    host=DB,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE TextAdventure")

"""
# Zur Testung
mycursor.execute("Show Databases")

for x in mycursor:
    print(x)
"""

#mycursor.execute("use TextAdventure")
#mycursor.execute("CREATE TABLE weapons (ID int, NAME VARCHAR(255), DAMAGE int, ACCURACY int, PRICE int, REACH int, DURABILITY int)")

"""
# Zur Testung

mycursor.execute("use Textdatabase")
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)
"""

player = load_player("ben")

mycursor.execute("use TAUsers")
#mycursor.execute("CREATE TABLE UserData (Name VARCHAR(100), Money int, MaxHealth int, MaxMana int, Health int, Mana int, Strength int, Weapon int)")
#sql = "INSERT INTO UserData (Name, Money, MaxHealth, MaxMana, Health, Mana, Strength, Weapon) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
#val = [(player.name, player.money, player.max_health, player.max_mana, player.health, player.mana, player.strength, player.weapon.id)]
print(f"UPDATE UserData SET MaxHealth = '%s' WHERE Name = '%s'" %(player.max_health, player.name))
#mycursor.executemany(sql, val)

#mydb.commit()

#print(mycursor.rowcount, "was inserted.")