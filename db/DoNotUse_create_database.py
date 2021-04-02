import mysql.connector
from ta_data.config import *

mydb = mysql.connector.connect(
    host=DB,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE TextAdventure")

"""
# Zur Testung
mycursor.execute("Show Databases")

for x in mycursor:
    print(x)
"""

mycursor.execute("use TextAdventure")
mycursor.execute("CREATE TABLE weapons (ID int, NAME VARCHAR(255), DAMAGE int, ACCURACY int, PRICE int, REACH int, DURABILITY int)")

"""
# Zur Testung

mycursor.execute("use Textdatabase")
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)
"""

#mycursor.execute("use Textdatabase")
sql = "INSERT INTO weapons (ID, NAME, DAMAGE, ACCURACY, PRICE, REACH, DURABILITY) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = [
  (0, 'Fist', 1, 1, 0, 0, -1),
  (1, 'Pebel', 1, 1, 0, 2, -1)
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")