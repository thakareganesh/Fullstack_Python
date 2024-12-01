import sqlite3 as sql
con = sql.connect('Amazon')
cur = con.cursor()
q1 = "update products set availability = ? where pid = ?"
availability = int(input("Enter number: "))
pid = int(input("Enter pid: "))
t1 = (availability,pid)
cur.execute(q1,t1)
print("record updated")
con.commit()
con.close()