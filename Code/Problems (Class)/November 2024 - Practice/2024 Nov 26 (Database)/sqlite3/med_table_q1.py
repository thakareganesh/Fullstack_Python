# Question: Medicine Table Created

import sqlite3 as sql
con = sql.connect("Amazon")
print("opened connection")
cur = con.cursor()
q = "create table product(MedId int primary key, MedName text, Cost real,Availability int, ExpDate date)"
cur.execute(q)
print("Table created")
con.close()
