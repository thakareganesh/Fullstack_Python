import pyodbc as sql
con = sql.connect(driver='Sql Server', server="GANESH\\SQLEXPRESS", database='Amazon1', user='Ganesh', password='82668')
cur = con.cursor()
q1 = "CREATE TABLE Customer(Cid int primary key,Cname varchar(20),Cgender char(1),CAmount Money)"
# q1 = "Drop table Customer"
cur.execute(q1)
con.commit()
con.close()