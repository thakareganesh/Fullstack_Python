import random
import pyodbc as sql

# Connect to the database
con = sql.connect(
    driver="Sql Server",
    server="GANESH\\SQLEXPRESS",
    database="Amazon1",
    user="Ganesh",
    password="82668"
)
cur = con.cursor()

# Fetch existing transaction IDs
cur.execute("SELECT tid FROM Transactions")  # Replace 'TransactionID' with the actual column name
rows = cur.fetchall()

# Extract IDs into a list
existing_ids = []
for row in rows:
    existing_ids.append(row[0])

# Optionally, convert to a set for faster lookups
existing_ids_set = set(existing_ids)
print(f"Existing IDs: {existing_ids_set}")

# Generate a unique transaction ID
tid_lists = list(range(1, 101))
random.shuffle(tid_lists)  # Shuffle to randomize the IDs

unique_tid = None
for tid_val in tid_lists:
    tid = f"T{tid_val}"
    if tid not in existing_ids_set:  # Check if the ID is unique
        unique_tid = tid
        break

if unique_tid:
    print(f"Unique Transaction ID: {unique_tid}")
    # Here you can insert the unique ID into the database or use it further
    # Example: Insert into the database (uncomment and modify if needed)
    # cur.execute("INSERT INTO Transactions (TransactionID, OtherColumn) VALUES (?, ?)", (unique_tid, 'OtherValue'))
    # con.commit()
else:
    print("No unique transaction ID available.")

# Close the connection
con.close()

