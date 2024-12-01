# Question 6: Display all available medicines

import pyodbc as sql
con = sql.connect(driver='Sql Server', server="GANESH\\SQLEXPRESS", database='Amazon1', user='Ganesh', password='82668')
cur = con.cursor()
query = "select * from Medicines"
cur.execute(query)
data = cur.fetchall()
print("MedID \tMedName \tCost \tAvalability \tExpDate")
for row in data:
    for col in row:
        print(col,end="   ")
    print()
con.close()

