# Menu Card - Project Building

print("Welcome to SHREE GANESH Hotel")

idaly = 40
dosa = 50
vada = 60
poori = 70

ch = "y"
finalBillAmt = 0

while(ch=="y"):
    print("""\t\tM E N U
    1.Idaly : 40 ₹
    2.Dosa  : 50 ₹
    3.Vada  : 60 ₹
    4.Poori : 70 ₹""")
    choice = int(input("Enter your choice: "))
    billAmt = 0
    if (choice >= 1 and choice <=4):
        if choice == 1:
            item_name = "Idaly"
            cost = idaly
        elif choice == 2:
            item_name = "Dosa"
            cost = dosa
        elif choice == 3:
            item_name = "Vada"
            cost = vada
        else:
            item_name = "Poori"
            cost = poori
        print(f"Cost of {item_name} is: {cost}")

        quantity = int(input("Enter Quantity: "))
        billAmt = cost * quantity
        print(f"Bill Amount is: {billAmt} ₹")
    else:
        print("Invalid Choice")
    ch = input("Do you want any other item(y/n): ")
    finalBillAmt = finalBillAmt + billAmt
print(f"Final Bill Amount is: {finalBillAmt} ₹")