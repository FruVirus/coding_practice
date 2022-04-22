# pylint: disable=C0114, E1121, R0204

# Third Party Library
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="cajunFRU1218",
)
print(mydb)
