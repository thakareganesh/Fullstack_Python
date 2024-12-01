# Question 2 v2: Read Medicine Name if available then print cost, read quantity from user then display billAmt
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
        cost = round(data[0][2],2)
        print("Cost is:",cost)
        quantity = int(input("How many sheets do you want: "))
        availability = data[0][3]
        if quantity < availability:
            billAmt = cost * quantity
            print("Bill Amount is:", billAmt)
        else:
            print(f"There are only {availability} Sheets available")
else:
    print("Medicine Not Available")
con.close()
