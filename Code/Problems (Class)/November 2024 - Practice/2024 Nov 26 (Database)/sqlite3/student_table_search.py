import sqlite3 as sql
con = sql.connect('Amazon')
print("Connection Opened")
cur = con.cursor()
q1 = "select * from Student Where sid = ?"
sid = int(input("Enter Hall-ticket Number: "))
cur.execute(q1,(sid,))
data = cur.fetchall()
if data:
    print("sid studentname \tgender chem bio phy total avg grade result")
    if data[0][0] == sid:
        for row in data:
            for col in row:
                print(col,end="\t")
            print()
else:
    print("Invalid Hallticket Number")
con.close()