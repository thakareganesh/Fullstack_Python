# Question 6: Display menu card as
"""
    1. Idly
    2. Dosa
    3. Vada
    4. Puri
    Enter your choice = 1
    Do you want to continue(y/n): y
    Enter your choice = 3
    Do you want to continue(y/n): n
    Your order is : ["Idly","Vada"]
"""

menu = """\tMenu Card
    1. Idly
    2. Dosa
    3. Vada
    4. Puri"""

print(menu)

order_list = []
ch1 = "y"
while ch1 == "y":
    ch = int(input("Enter your choice: "))
    if (ch>0 and ch<5):
        if ch == 1:
            order_list.append("Idly")
        elif ch == 2:
            order_list.append("Dosa")
        elif ch == 3:
            order_list.append("Vada")
        else:
            order_list.append("Puri")
    else:
        print("Invalid choice")
    ch1 = input("Do you want to continue(y/n): ")

print("Your order is:",order_list)