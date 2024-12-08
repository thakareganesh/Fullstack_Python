import pyodbc as sql
con = sql.connect(driver="SQL Server",server="GANESH\\SQLEXPRESS",database="Amazon1", user="Ganesh", password="82668")
cur = con.cursor()
q2="select * from products"
cur.execute(q2)
pid = cur.fetchone()[0]
pname = cur.fetchall()
print(pid,pname)
con.commit()
con.close()