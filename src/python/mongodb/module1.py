# pylint: disable=C0114, E1121, R0204

# Third Party Library
import mysql.connector

# Python MySQL #

# MySQL Get Started
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="cajunFRU1218",
    database="mydatabase",
)
print(mydb)
print()

# MySQL Create Database
mycursor = mydb.cursor()
try:
    mycursor.execute("CREATE DATABASE mydatabase")
except mysql.connector.DatabaseError:
    pass
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
print()

# MySQL Create Table
# mycursor.execute(
#     "CREATE TABLE customers "
#     "(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))"
# )
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# mycursor.execute(
#     "CREATE TABLE users "
#     "(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), fav INT)"
# )
# mycursor.execute(
#     "CREATE TABLE products "
#     "(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))"
# )
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
print()

# MySQL Insert
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
    ("Peter", "Lowstreet 4"),
    ("Amy", "Apple st 652"),
    ("Hannah", "Mountain 21"),
    ("Michael", "Valley 345"),
    ("Sandy", "Ocean blvd 2"),
    ("Betty", "Green Grass 1"),
    ("Richard", "Sky st 331"),
    ("Susan", "One way 98"),
    ("Vicky", "Yellow Garden 2"),
    ("Ben", "Park Lane 38"),
    ("William", "Central st 954"),
    ("Chuck", "Main Road 989"),
    ("Viola", "Sideway 1633"),
]  # type: ignore
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("Michelle", "Blue Village")
# mycursor.execute(sql, val)
# mydb.commit()
# print("1 record inserted, ID:", mycursor.lastrowid)
# print()

# MySQL Select
# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
# mycursor.execute("SELECT name, address FROM customers")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchone()
# print(myresult)
# myresult = mycursor.fetchmany(5)
# print(myresult)
# mycursor.fetchall()
# print()

# MySQL Where
# sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
# sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
# print()

# MySQL Order By
# sql = "SELECT * FROM customers ORDER BY name"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
# sql = "SELECT * FROM customers ORDER BY name DESC"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
# print()

# MySQL Delete
# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")
# sql = "DELETE FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )
# mycursor.execute(sql, adr)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")
# print()

# MySQL Drop Table
# mycursor = mydb.cursor()
# sql = "DROP TABLE customers"
# mycursor.execute(sql)
# mycursor = mydb.cursor()
# sql = "DROP TABLE IF EXISTS customers"
# mycursor.execute(sql)

# MySQL Update
mycursor = mydb.cursor()
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")
mycursor = mydb.cursor()
sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")
print()

# MySQL Limit
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers LIMIT 5")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print()
