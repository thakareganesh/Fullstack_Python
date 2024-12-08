import os

import pyodbc as sql

# Retrieve environment variables
driver = os.getenv("DB_DRIVER")
server = os.getenv("DB_SERVER")
database = os.getenv("DB_DATABASE")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

print(f"Database Driver  : {driver}")
print(f"Database Server  : {server}")
print(f"Database Database: {database}")
print(f"Database username: {user}")
print(f"Database password: {password}")

try:
    con = sql.connect(driver=driver,server=server,database=database,user=user,password=password)
    cur = con.cursor()
    print(con)
except sql.Error as e:
    print("Error Connecting to the Database")
    print("Error Cause:",e)