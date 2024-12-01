import sqlite3 as sql
con = sql.connect("Amazon")
print("opened connection")
cur = con.cursor()

# For Update all records at once
q_update = "update product set Availability = 10"
cur.execute(q_update)
con.commit()
print("Table Updated")
con.close()

# For inserting records in product table
# q_insert = "insert into product values(1126,'Cetirizine',15,10,'2024-12-31')"
# cur.execute(q_insert)
# con.commit()
# print("Record Inserted")
# con.close()