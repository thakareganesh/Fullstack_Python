import sqlite3 as sql
con = sql.connect("Amazon")
cur = con.cursor()
q2 = "insert into emp values(105,'Mukesh',28000.0)"
cur.execute(q2)
con.commit()
print("Record inserted")
con.close()