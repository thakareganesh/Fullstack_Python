# Question 5: read medicine name and then delete record
import sqlite3 as sql
con = sql.connect('Amazon')
cur = con.cursor()
query = "select * from product where MedName = ?"
MedName = input("Enter Medicine Name: ").capitalize()
t1 = (MedName,)
cur.execute(query,t1)
data = cur.fetchall()
if data:
    if data[0][1] == MedName:
        print("Medicine Available")
        query = "delete from product where MedName = ?"
        cur.execute(query,t1)
        con.commit()
        print(f"Record of Medicine {MedName} is deleted")
else:
    print("Medicine is not available")