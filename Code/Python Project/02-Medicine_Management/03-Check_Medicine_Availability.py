# question 1: read the medicine name from the user and then check available or not

import pyodbc as sql
con = sql.connect(driver='Sql Server', server="GANESH\\SQLEXPRESS", database='Amazon1', user='Ganesh', password='82668')
cur = con.cursor()
q = "select * from Medicines where MedName=?"
MedName = input("Enter Medicine Name: ").title()
t1 = (MedName,)
cur.execute(q,t1)
data = cur.fetchall()
if data:
    if data[0][1] == MedName:
        print("Medicine Available")
else:
    print("Medicine Not Available")
con.close()
