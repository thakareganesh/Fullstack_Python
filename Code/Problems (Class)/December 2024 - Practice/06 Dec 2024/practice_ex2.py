# Insert Records In the Candidate Table
import pyodbc as sql
con = sql.connect(driver="SQL Server",server="GANESH\\SQLEXPRESS",database="Amazon1", user="Ganesh", password="82668")
cur = con.cursor()
ch = "y"
cid = int(input("Enter Candidates ID: "))
q = "Select * from Candidates where cid = ?"
cur.execute(q,(cid,))
data = cur.fetchone()
if data:
    print("Record already Exists")
else:
    print("Record not Found, So you can insert new Records")
    while ch == 'y':
        q1 = "exec sp_ins_candidates ?,?,?"
        cname = input("Enter Candidate Name: ") .title()
        gender = input("Enter your gender(M/F): ").capitalize()
        cur.execute(q1,(cid,cname,gender))
        ch = input("Do you want to enter more records: ").lower()
con.commit()
con.close()