import pyodbc as sql
import random
con = sql.connect(driver='Sql Server', server="GANESH\\SQLEXPRESS", database='Amazon1', user='Ganesh', password='82668')
cur = con.cursor()

tid_lists = []
for i in range(1,101):
    val = random.randint(1,100)
    if val not in tid_lists:
        tid_lists.append(val)

def Deposit():
    dAmt = float(input("How much money you want to Deposit: "))
    if dAmt > 0:
        q1 = "exec sp_updateD_Customer ?,?"
        t1 = (dAmt, Cid)
        cur.execute(q1, t1)
        q2 = "exec sp_ins_trans ?,?,?,?"
        Tid = tid_lists[0]
        f_Tid = f"T{Tid}"
        tid_lists.pop(0)
        Ctype = "D"
        t2 = (f_Tid, Cid, Ctype, dAmt)
        cur.execute(q2, t2)
        con.commit()
        print(f"{dAmt}₹ is Deposited to Your Account")
    else:
        print("Transaction Unsuccessful: Deposit Amount Must be More than Rs.0₹")

def WithDraw():
    query = "exec sp_dis_customer ?"
    cur.execute(query,(Cid,))
    CAmt = round(cur.fetchone()[3],2)
    wAmt = float(input("How much money you want to withdraw: "))
    if wAmt > 0:
        if wAmt < CAmt:
            q1 = "exec sp_updateW_Customer ?,?"
            t1 = (wAmt, Cid)
            cur.execute(q1, t1)
            q2 = "exec sp_ins_trans ?,?,?,?"
            Tid = tid_lists[0]
            f_Tid = f"T{Tid}"
            tid_lists.pop(0)
            Ctype = "W"
            t2 = (f_Tid, Cid, Ctype, wAmt)
            cur.execute(q2, t2)
            con.commit()
            print(f"{wAmt}₹ is Withdrawn From Your Account")
        else:
            print("Transaction Declined: You have insufficient funds to complete this operation.")
            print("\t\t\t\t\t  Please check your balance and try again.")
    else:
        print("Transaction Unsuccessful: Withdraw Amount Must be More than Rs.0₹")

def BalEnq():
    q3 = "exec sp_dis_customer ?"
    cur.execute(q3,(Cid,))
    record = cur.fetchall()
    balance = round(record[0][3],2)
    print(f"Balance of '{Cname}' is : {balance}₹")

def miniStmt():
    q5 = "exec sp_dis_transactions ?"
    cur.execute(q5,(Cid,))
    record = cur.fetchall()
    print("Tid \t\tCid \tType \tTAmount")
    for row in record:
        for col in row:
            print(col,end="\t\t")
        print()

def ShowAccDetails():
    q5 = "exec sp_dis_customer ?"
    t5 = (Cid,)
    cur.execute(q5,t5)
    record = cur.fetchone()
    if record:
        CAmount = round(record[3],2)
        print("Your Account Details:")
        print("Cid \tCname \t\tCgender CAmount")
        print(f"{Cid}  {Cname}   {Cgender} \t{CAmount}")

def Bank_Options():
    print("1.Deposit \n2.Withdraw\n3.Balance Enquiry\n4.Mini Statement\n5.Show Account Details \n6.Exit")


print("Welcome to State Bank of India")
Cid = input("Enter Your ID: ")
q0 = "EXEC sp_dis_customer ?"
cur.execute(q0,(Cid,))
data = cur.fetchall()
if data:
    Cname = data[0][1]
    Cgender = data[0][2]
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
        ch = input("Do you want to perform any other operations? (yes/no): ").lower()
else:
    print("Unauthorized Access: You are not an authorized user of our bank.")
    print("Please contact your branch for further assistance.")
con.close()
print("Logging out. Goodbye!")