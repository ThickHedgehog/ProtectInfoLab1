import sqlite3

db = sqlite3.connect("database.db")
cur = db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Users(ID INT, Login TEXT, Password TEXT, Banned INT, Limited INT)")
cur.execute(f"INSERT INTO Users(ID, Login, Password, Banned, Limited) VALUES (?, ?, ?, ?, ?)", (0, "ADMIN", "", 0, 0))
db.commit()
cur.close()
db.close()