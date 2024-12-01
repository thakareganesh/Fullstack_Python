# Student Table Question 1: Create Table

import sqlite3 as sql
con = sql.connect('Amazon')
cur = con.cursor()
q1 = "Create table Student(sid int primary key,sname text,gender text,s1 int, s2 int, s3 int, total int, avg real,grade text, result text)"
cur.execute(q1)
con.commit()
con.close()