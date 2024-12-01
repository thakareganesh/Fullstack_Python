# Question 5: read medicine name and then delete record
import pyodbc as sql
con = sql.connect(driver='Sql Server', server="GANESH\\SQLEXPRESS", database='Amazon1', user='Ganesh', password='82668')
cur = con.cursor()
query = "select * from Medicines where MedName = ?"
MedName = input("Enter Medicine Name: ").title()
t1 = (MedName,)
cur.execute(query,t1)
data = cur.fetchall()
if data:
    if data[0][1] == MedName:
        print("Medicine Available")
        query = "delete from Medicines where MedName = ?"
        cur.execute(query,t1)
        con.commit()
        print(f"Record of Medicine {MedName} is deleted")
else:
    print("Medicine is not available")