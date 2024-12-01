import sqlite3 as sql
con = sql.connect('Amazon')
cur = con.cursor()
q = "create table products(pid int primary key,pname text,cost real,availability int, expdate date)"
cur.execute(q)
con.close()