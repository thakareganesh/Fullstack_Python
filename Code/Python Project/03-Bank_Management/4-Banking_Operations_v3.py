import pyodbc as sql
import random
con = sql.connect(driver='Sql Server', server="GANESH\\SQLEXPRESS", database='Amazon1', user='Ganesh', password='82668')
cur = con.cursor()
def Deposit():
    dAmt = float(input("How much money you want to Deposit: "))
    q1 = "UPDATE Customer SET CAmount = CAmount + ? where Cid = ?"
    t1 = (dAmt, Cid)
    cur.execute(q1, t1)
    q2 = "Insert Into Transactions values(?,?,?,?)"
    Tid = random.randint(1, 100)
    f_Tid = f"T{Tid}"
    Ctype = "D"
    t2 = (f_Tid, Cid, Ctype, dAmt)
    cur.execute(q2, t2)
    con.commit()
    print(f"{dAmt}₹ is Deposited to Your Account")

def WithDraw():
    cAmt = round(data[0][3],2) #Customer Account Balance
    wAmt = float(input("How much money you want to withdraw: "))
    if wAmt < cAmt:
        q1 = "UPDATE Customer SET CAmount = CAmount - ? where Cid = ?"
        t1 = (wAmt, Cid)
        cur.execute(q1, t1)
        q2 = "Insert Into Transactions values(?,?,?,?)"
        Tid = random.randint(1, 100)
        f_Tid = f"T{Tid}"
        Ctype = "W"
        t2 = (f_Tid, Cid, Ctype, wAmt)
        cur.execute(q2, t2)
        con.commit()
        print(f"{wAmt}₹ is Withdrawn From Your Account")
    else:
        print("Transaction declined: You have insufficient funds to complete this operation.")
        print("\t\t\t\t\t  Please check your balance and try again.")

def BalEnq():
    q3 = "Select * from Customer where Cid = ?"
    t3 = (Cid,)
    cur.execute(q3,t3)
    record = cur.fetchall()
    balance = record[0][3]
    name = record[0][1]
    balance = round(balance,2)
    print(f"Balance of '{name}' is : {balance}")

def miniStmt():
    q5 = "Select * From Transactions where Cid = ?"
    t5 = (Cid,)
    cur.execute(q5,t5)
    record = cur.fetchall()
    print("Tid \tCid Type TAmount")
    for row in record:
        for col in row:
            print(col,end=' ')
        print()

def ShowAccDetails():
    q5 = "Select * From Customer where Cid = ?"
    t5 = (Cid,)
    cur.execute(q5,t5)
    record = cur.fetchall()
    if record:
        print("Your Account Details:")
        print("Cid \tCname \t Cgender \tCAmount")
        Cgender = record[0][2]
        CAmount = round(record[0][3],2)
        print(f"{Cid}  {Cname}   {Cgender} \t\t{CAmount}")
        # for row in record:
        #     for col in row:
        #         print(col,end='\t')
        #     print()
    else:
        print(f"Record Not Found to Cid {Cid}")

def Bank_Options():
    print("1.Deposit \n2.Withdraw\n3.Balance Enquiry\n4.Mini Statement\n5.Show Account Details \n6.Exit")


print("Welcome to State Bank of India")
Cid = input("Enter Your ID: ")
q0 = "Select * from Customer where cid= ?"
cur.execute(q0,(Cid,))
data = cur.fetchall()
if data:
    Cname = data[0][1]
    print(f"You're Welcome '{Cname.upper()}'")
    ch = "yes"
    while ch == "yes":
        print("Choose Below options:")
        Bank_Options()
        options = int(input("Choose Your Option from above List: "))
        if options >= 1 and options <= 6:
            if options == 1:
                Deposit()
            elif options == 2:
                WithDraw()
            elif options == 3:
                BalEnq()
            elif options == 4:
                print("Mini Statement For Your Account")
                miniStmt()
            elif options == 5:
                ShowAccDetails()
            else:
                print("Thank you for using our services!")
                break
        else:
            print("Invalid Selection of Option. Please Try again!")
            options = int(input("Choose Your Option from above List: "))

        ch = input("Do you want to perform any other operations? (yes/no): ").lower()
else:
    print("Unauthorized Access: You are not an authorized user of our bank.")
    print("Please contact your branch for further assistance.")
con.close()
print("Logging out. Goodbye!")