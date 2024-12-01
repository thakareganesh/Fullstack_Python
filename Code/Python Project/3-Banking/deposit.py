import pyodbc as sql
con = sql.connect(driver='Sql Server', server="GANESH\\SQLEXPRESS", database='Amazon1', user='Ganesh', password='82668')
cur = con.cursor()
def Deposit():
    dAmt = float(input("How much money you want to deposit: "))
    q1 = "UPDATE Customer SET CAmount = CAmount + ? where Cid = ?"
    t1 = (dAmt,Cid)
    cur.execute(q1,t1)
    con.commit()
    print(f"{dAmt} is Deposited in Your Account")
tid = 100
def DepInsert():
    q2 = "Insert into Transactions values(?,?,?,?)"



con.commit()
con.close()