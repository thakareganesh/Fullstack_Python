import sqlite3 as sql
con = sql.connect('Amazon')
cur = con.cursor()
q = "insert into products values(101,'Ganesh',120,15,'2024-12-31')"

cur.execute(q)
con.commit()
con.close()