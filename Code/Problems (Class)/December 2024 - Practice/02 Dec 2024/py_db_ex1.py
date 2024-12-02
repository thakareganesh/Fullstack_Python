import pyodbc as sql
con = sql.connect(Driver="SQL Server", Server="GANESH\\SQLEXPRESS", database="Amazon1", user="Ganesh", password='82668')
cur = con.cursor()
query = "select * from Transactions"
cur.execute(query)
data = cur.fetchall()
con.close()