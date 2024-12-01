# question 3: read quantity from user then display billAmt as well as update availability
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
        # print("Medicine Name:",MedName)
        print("Cost is:",cost)
        # print("Medicine Availability:",data[0][3])
        quantity = int(input("How many sheets do you want: "))
        availability = data[0][3]
        if quantity <= availability:
            query = "update Medicines set Availability = ? where MedName = ?"
            remaining_sheets = availability - quantity
            t2 = (remaining_sheets,MedName)
            cur.execute(query,t2)
            print(f"Availability records of {MedName} updated")
            con.commit()
            billAmt = cost * quantity
            print("Bill Amount is:", billAmt)
        else:
            print(f"There are only {availability} Sheets of {MedName} available")
else:
    print("Medicine Not Available")
con.close()
