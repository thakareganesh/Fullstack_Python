import sqlite3 as sql
con = sql.connect("Amazon")
cur = con.cursor()
q1 = "insert into product values(1121,'Dolo',20,10,'2024-12-31')"
cur.execute(q1)
q2 = "insert into product values(1122,'Crocine',50,10,'2024-12-31')"
cur.execute(q2)
q3 = "insert into product values(1123,'Nicif Cold And Flue',40,10,'2024-12-31')"
cur.execute(q3)
q4 = "insert into product values(1124,'Paracetamol',60,10,'2024-12-31')"
cur.execute(q4)
q5 = "insert into product values(1125,'Cetirizine',25,10,'2024-12-31')"
cur.execute(q5)
con.commit()
print("Record inserted")
con.close()