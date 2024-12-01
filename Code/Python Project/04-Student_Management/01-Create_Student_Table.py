# Student Table Question 1: Create Table

import pyodbc as sql
con = sql.connect(driver='Sql Server', server="GANESH\\SQLEXPRESS", database='Amazon1', user='Ganesh', password='82668')
cur = con.cursor()
print("Connection Opened")
q1 = "Create table Student(sid int primary key,sname varchar(20),gender varchar(6),biology int, chemistry int, physics int, total int, avg money,grade varchar(4), result varchar(6))"
cur.execute(q1)
con.commit()
print("Student table Created")
con.close()
print("Connection Closed")