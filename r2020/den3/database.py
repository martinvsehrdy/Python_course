import sqlite3


db_file = "../../webserver/database.db"
conn = sqlite3.connect(db_file)
cursor = conn.cursor()


ret = cursor.execute("SELECT * FROM author").fetchall()
print(len(ret), ret)
ret = cursor.execute("SELECT * FROM article").fetchall()
print(len(ret), ret)

cursor.execute("INSERT INTO author (name) VALUES(?)", ("Martin Cerny", ))

conn.commit()
conn.close()
