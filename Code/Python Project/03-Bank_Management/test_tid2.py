import pyodbc as sql
import random
import os

# Database connection details
driver = os.getenv("DB_Driver")
server = os.getenv("DB_Server")
database = os.getenv("DB_Database")
user = os.getenv("DB_User")
password = os.getenv("DB_Password")

# Establish connection
con = sql.connect(driver=driver, server=server, database=database, user=user, password=password)
cur = con.cursor()

# Fetch existing transaction IDs
def unique_tid():

    query = "SELECT Tid FROM transactions"
    cur.execute(query)
    tid_records = cur.fetchall()
    tid = 0
    # Create a list of existing transaction IDs
    tid_list = []
    for record in tid_records:
        for value in record:
            tid_list.append(value)
    unique = False
    while not unique:
        tid = f"T{random.randint(1, 101)}"
        if tid not in tid_list:
            unique = True
    return tid

tid = unique_tid()
print(tid)

# Close the connection
con.close()
