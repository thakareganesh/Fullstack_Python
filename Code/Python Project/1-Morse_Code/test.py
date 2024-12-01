import pandas as pd
from decimal import Decimal

# Given data
data = [(101, 'Ganesh Thakare', 'M', Decimal('5000.0000'))]

# Define column names
columns = ['ID', 'Name', 'Gender', 'Amount']

# Create a DataFrame
df = pd.DataFrame(data, columns=columns)

# Display the DataFrame
print(df)