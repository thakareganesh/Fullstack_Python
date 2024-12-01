import sqlite3 as sql

# Connect to the database
con = sql.connect('Amazon')
cur = con.cursor()

# Get employee ID input
eid = int(input("Enter emp id: "))
t1 = (eid,)

# Fetch all records matching the given ID
fetch_query = "SELECT * FROM emp WHERE eid = ?"
cur.execute(fetch_query, t1)
records = cur.fetchall()  # Get all matching rows

if records:
    # If records exist, delete the record
    delete_query = "DELETE FROM emp WHERE eid = ?"
    cur.execute(delete_query, t1)
    con.commit()
    print("Record deleted")
else:
    print("No record found with the given ID")

# Close the connection
con.close()
