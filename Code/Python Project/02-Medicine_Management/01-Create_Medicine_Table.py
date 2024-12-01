# Question: Medicine Table Created

import pyodbc as sql
con = sql.connect(driver='Sql Server', server="GANESH\\SQLEXPRESS", database='Amazon1', user='Ganesh', password='82668')
print("opened connection")
cur = con.cursor()
q = "create table Medicines(MedId int primary key, MedName varchar(20), Cost money,Availability int, ExpDate date)"
cur.execute(q)
con.commit()
print("Table created")
con.close()
print("Connection Closed")
