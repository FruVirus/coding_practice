# pylint: disable=C0114, E1121, R0204

# Third Party Library
from mysql.connector import Error, connect

try:
    with connect(
        host="localhost",
        user="root",
        password="cajunFRU1218",
    ) as connection:
        print(connection)
except Error as e:
    print(e)
