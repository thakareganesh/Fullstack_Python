import pyodbc as sql
con = sql.connect(driver='SQL Server', server='GANESH\\SQLEXPRESS',database='Amazon1', user='Ganesh',password='82668')
print(con)
con.close()