# Question 6: Display all available medicines

import sqlite3 as sql
con = sql.connect('Amazon')
cur = con.cursor()
query = "select * from product"
cur.execute(query)
data = cur.fetchall()
print("MedID \tMedName \tCost \tAvalability \tExpDate")
for row in data:
    for col in row:
        print(col,end="\t")
    print()
con.close()

