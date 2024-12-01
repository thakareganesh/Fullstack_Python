import pyodbc as sql
con = sql.connect(driver='Sql Server', server="GANESH\\SQLEXPRESS", database='Amazon1', user='Ganesh', password='82668')
print("Opened Connection With Database")
cur = con.cursor()
ch = "yes"
while ch == "yes":
    Cid = int(input("Insert Customer ID: "))
    Cname = input("Enter Customer Name: ").title()
    Cgender = input("Enter Customer Gender(M/F): ").capitalize()
    CAmount = (input("Enter Amount to Deposit: "))
    q1 = "INSERT INTO Customer values(?,?,?,?)"
    t1 = (Cid,Cname,Cgender,CAmount)
    cur.execute(q1,t1)
    con.commit()
    print(f"Record for Name: {Cname} is inserted successfully")
    ch = input('Do you want to insert any other record(yes/no): ').lower()
con.close()
print("Connection Closed")