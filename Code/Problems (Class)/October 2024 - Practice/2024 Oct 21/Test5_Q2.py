# Question 2:

# Declaring values of Dishes and quantity as zero
IDLY = 40
PURI = 50
DOSA = 60
VADA = 30
quantity = 0

# Displaying Choice of Menu to Customer
Menu = """
         Menu
    1. IDLY = 40 Rs
    2. PURI = 50 Rs
    3. DOSA = 60 Rs
    4. VADA = 30 Rs
    """
print(Menu)

# Taking choice from Customer
choice = int(input("Enter your Choice: "))

# Logic for the customer choice
if choice == 1:
    choice = IDLY
    dish = "IDLY"
    quantity = int(input("Enter Quantity: "))
elif choice == 2:
    choice = PURI
    dish = "PURI"
    quantity = int(input("Enter Quantity: "))
elif choice == 3:
    choice = DOSA
    dish = "DOSA"
    quantity = int(input("Enter Quantity: "))
elif choice == 4:
    choice = VADA
    dish = "VADA"
    quantity = int(input("Enter Quantity: "))
else:
    choice = 0
    dish = "Invalid Dish"
    print("Sorry..! Your listed item is not available.")

# Calculating final bill and showing details
billAmt = choice * quantity
print("Cost of",dish,"is:",choice)
print("Bill amount is:",billAmt)
