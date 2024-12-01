import pyodbc as sql
con = sql.connect(driver='Sql Server', server="GANESH\\SQLEXPRESS", database='Amazon1', user='Ganesh', password='82668')
cur = con.cursor()
q1 = "CREATE TABLE Transactions(Tid Char(5) primary key,Cid int foreign key references Customer(Cid),Ttype char(1),TAmount Money)"
# q1 = "Drop Table Transactions"
cur.execute(q1)
con.commit()
con.close()