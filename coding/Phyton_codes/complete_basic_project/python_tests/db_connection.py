import sqlite3

connection  = sqlite3.connect("b_database.bd")

cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS user(name, address, phone)")

res = cursor.execute("select * from user")
res.fetchone()

print(res)