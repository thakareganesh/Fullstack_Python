

idly = 1
puri = 2
dosa = 3
vada = 4
choice = int(input("Enter your choice: "))
if choice >= 1 and choice <= 4:
    if choice == 1:
        cost = 40
    elif choice == 2:
        cost = 60
    elif choice == 3:
        print("1.Normal Dosa\n2.Masala Dosa\n3.Onion Dosa")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            cost = 70
        elif choice == 2:
            cost = 80
        elif choice == 3:
            cost = 100
        else:
            print("Invalid Selection for Dosa Category")
    elif choice == 4:
        cost = 30
    quantity = int(input("Enter your quantity: "))
    billAmt = cost * quantity
    print("Bill Amount is:",billAmt)
    if billAmt > 300:
        dis = 10
        disAmt = billAmt * dis / 100
        print("Discount is:",dis,"%")
        print("Discount amount is:",disAmt)

        final_bill = billAmt - disAmt
        print("Final Bill is:",final_bill)
else:
    print("Invalid input")
