import sqlite3 as sql
con = sql.connect("Amazon")
print("opened conncetion")
cur = con.cursor()
q = "create table emp(eid int primary key, ename text, salary real)"
cur.execute(q)
con.close()
