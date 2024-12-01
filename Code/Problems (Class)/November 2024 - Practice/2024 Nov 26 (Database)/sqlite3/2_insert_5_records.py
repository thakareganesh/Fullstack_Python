import sqlite3 as sql
con = sql.connect('Amazon')
cur = con.cursor()
q1 = "insert into products values(111,'Mobile',25000,10,'2035-12-31')"
q2 = "insert into products values(222,'Pendrive',800,8,'2024-07-12')"
q3 = "insert into products values(333,'Laptop',30000.0,3,'2026-11-15')"
q4 = "insert into products values(444,'Keyboard',1200.0,5,'2027-08-19')"
q5 = "insert into products values(555,'Mouse',600.0,7,'2028-02-30')"
cur.execute(q1)
cur.execute(q2)
cur.execute(q3)
cur.execute(q4)
cur.execute(q5)
con.commit()
con.close()