# Question 4: Read multiple medicine names and prepare final bill amount
import pyodbc as sql
con = sql.connect(driver='Sql Server', server="GANESH\\SQLEXPRESS", database='Amazon1', user='Ganesh', password='82668')
cur = con.cursor()
final_billAmt = 0
ch = "y"
while ch == "y":
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
            try:
                quantity = int(input("How many sheets do you want: "))
            except ValueError:
                print("Quantity should be in number only.")
            else:
                availability = data[0][3]
                if quantity <= availability:
                    query = "update Medicines set Availability = ? where MedName = ?"
                    remaining_sheets = availability - quantity
                    t2 = (remaining_sheets, MedName)
                    cur.execute(query, t2)
                    print(f"Availability records of {MedName} updated")
                    con.commit()
                    billAmt = cost * quantity
                    final_billAmt = final_billAmt + billAmt
                    print(f"Bill Amount for {MedName} is: {billAmt}")
                else:
                    print(f"There are only {availability} Sheets available")
    else:
        print("Medicine Not Available")
    ch = input("Do you want any other medicine(y/n): ")
print(f"Final bill is : {final_billAmt}")
con.close()
