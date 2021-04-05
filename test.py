import os, hashlib
import mysql.connector
from ta_data.config import *

mydb = mysql.connector.connect(host=DB, port=DB_PORT, user=DB_USER, password=DB_PASSWORD)

from ta_data.config import *

mycursor = mydb.cursor()
mycursor.execute("USE TAUsers")
mycursor.execute("SELECT * FROM UserDataDev WHERE Familyname = 'Bennexy' AND Name = 'Ben'")
player_data = mycursor.fetchall()
print(player_data)
