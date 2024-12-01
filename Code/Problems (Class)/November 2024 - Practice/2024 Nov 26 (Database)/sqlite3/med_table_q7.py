# Question 5: read medicine name and then delete record
import sqlite3 as sql
con = sql.connect('Amazon')
cur = con.cursor()
query = "delete from product where MedName = ?"
MedName = input("Enter Medicine Name: ").capitalize()
t1 = (MedName,)
cur.execute(query,t1)
con.commit()
print(f"Record of {MedName} is deleted")
con.close()