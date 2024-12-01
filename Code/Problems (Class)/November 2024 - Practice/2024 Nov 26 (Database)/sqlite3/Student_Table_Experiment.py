import sqlite3 as sql
con = sql.connect('Amazon')
cur = con.cursor()
q = "delete from Student" #deleted all records
cur.execute(q)
con.commit()
con.close()