import sys
sys.path.append(".")
import mysql.connector, hashlib
from ta_data.config import *
from ta_data.src.character import load_player
from ta_data.players.player import Player

mydb = mysql.connector.connect(
    host=DB,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD
)

mycursor = mydb.cursor()



def enemies_init():
  mycursor.execute("CREATE DATABASE Enemies")
  mycursor.execute("use Enemies")
  mycursor.execute("CREATE TABLE Human (ID int, Name VARCHAR(100), Money int, MaxHealth int, MaxMana int, Health int, Mana int, Strength int, Weapon int)")
  mycursor.execute("CREATE TABLE Elf (ID int, Name VARCHAR(100), Money int, MaxHealth int, MaxMana int, Health int, Mana int, Strength int, Weapon int)")
  mycursor.execute("CREATE TABLE Ork (ID int, Name VARCHAR(100), Money int, MaxHealth int, MaxMana int, Health int, Mana int, Strength int, Weapon int)")
  mydb.commit()

def enemies_human():
  mycursor.execute("use Enemies")
  sql = "INSERT INTO Human (ID, Name, Money, MaxHealth, MaxMana, Health, Mana, Strength, Weapon) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
  val_list = [
    [(0, "Bandit", 2, 200, 10, 200, 10, 1, 1)], 
    [(1, "Strong Bandit", 4, 250, 10, 200, 10, 2, 1)],
    [(2, "Tanky Bandit", 4, 350, 10, 300, 10, 1, 1)]
    ]
  for val in val_list:
    mycursor.executemany(sql, val)
  mydb.commit()

def player_init():
  player = Player("Bennexy", "Ben2")
  mycursor.execute("use TAUsers")
  #mycursor.execute("CREATE TABLE UserDataDev (Familyname VARCHAR(100), Password VARCHAR(100), Name VARCHAR(100), Money int, MaxHealth int, MaxMana int, Health int, Mana int, Strength int, Weapon int)")
  sql = "INSERT INTO UserDataDev (Familyname, Password, Name, Money, MaxHealth, MaxMana, Health, Mana, Strength, Weapon) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
  val = [(player.family_name, hash("passtest"), player.name, player.money, player.max_health, player.max_mana, player.health, player.mana, player.strength, player.weapon.id)]
  mycursor.executemany(sql, val)

  mydb.commit()

player_init()

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

#player = load_player("ben")





#print(mycursor.rowcount, "was inserted.")