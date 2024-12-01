import sqlite3 as sql
con = sql.connect('Amazon')
cur = con.cursor()
q = "delete from emp where eid = ?"
eid = int(input("Enter emp id: "))
t1 = (eid,)
cur.execute(q,t1)
con.commit()
print("Record deleted")
con.close()