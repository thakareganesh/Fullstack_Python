# Question 4: Read item from customer then add all items to order list, then display customer order

order_list = []
ch = "y"

while ch == "y":
    dish = input("Enter item name: ")
    order_list.append(dish)
    ch = input("Do you want to continue(y/n: ")
    
print("Your order is:",order_list)