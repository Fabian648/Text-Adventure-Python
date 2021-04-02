import sys
sys.path.append(".")
import mysql.connector
from ta_data.config import *

mydb = mysql.connector.connect(
    host=DB,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD
)

def read_database(ID, FIELD, KIND):
    mycursor = mydb.cursor()
    mycursor.execute("USE " + str(DB_NAME))
    mycursor.execute("SELECT " + FIELD + " FROM " + KIND + " WHERE ID = " + str(ID))


    myresult = mycursor.fetchone()
    
    print(myresult)

read_database("*", "*", "melee_weapons")