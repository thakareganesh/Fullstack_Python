bio = int(input("Enter your biology marks: "))
chem = int(input("Enter your chemistry marks: "))
phy = int(input("Enter your physics marks: "))
no_of_sub = 3

if (bio>=35 and chem>=35 and phy >= 35):
    total = bio + chem + phy
    avg = total / no_of_sub
    print("Total marks:",total)
    print("Average is:",avg)
else:
    print("Better luck next time.")
