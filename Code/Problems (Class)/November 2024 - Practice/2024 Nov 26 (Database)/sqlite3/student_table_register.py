# Task 1
import sqlite3 as sql
con = sql.connect('Amazon')
print("Connection Opened")
cur = con.cursor()
ch = "y"
while ch == "y":
    q1 = "insert into Student values(?,?,?,?,?,?,?,?,?,?)"
    sid = int(input("Enter Student ID: "))
    sname = input("Enter your Name: ").title()
    gender = input("Enter your Gender: ").capitalize()
    chem = int(input("Enter Chemistry Marks: "))
    bio = int(input("Enter Biology Marks: "))
    phy = int(input("Enter Physics Marks: "))
    tot = chem + bio + phy
    num_of_sub = 3
    average= tot/num_of_sub
    avg = round(average,2)
    grade = ""
    if chem >= 35 and bio >=35 and phy >=35:
        result = "Pass"
        if avg >= 90 and avg <=100:
            grade= "O"
        elif avg >=80 and avg < 90:
            grade="A+"
        elif avg >= 70 and avg <80:
            grade = "A"
        elif avg >= 60 and avg<70:
            grade = "B"
        elif avg >= 50 and avg < 60:
            grade = "C"
        else:
            grade = "D"
    else:
        result = "Fail"
        grade = "F"
    t1 = (sid,sname,gender,chem,bio,phy,tot,avg,grade,result)
    cur.execute(q1,t1)
    con.commit()
    ch =input("Do you want to insert more student records(y/n): ").lower()
    print("Record Updated")
con.close()
print("Connection Closed")

