import pyodbc as sql
con = sql.connect(driver='SQL Server', server='GANESH\\SQLEXPRESS',database='Amazon1', user='Ganesh',password='82668')
cur = con.cursor()
q1 = "select * from Dept"
cur.execute(q1)
data = cur.fetchall()
print(data)
con.commit()
con.close()