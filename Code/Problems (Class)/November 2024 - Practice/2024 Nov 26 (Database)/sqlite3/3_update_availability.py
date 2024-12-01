import sqlite3 as sql
con = sql.connect('Amazon')
cur = con.cursor()
q1 = "update products set availability = 12 where pid = 111"
cur.execute(q1)
con.commit()
con.close()