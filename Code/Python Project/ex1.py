ch="y"
order_list=[]
def addItems(ch,order_list):
     while ch == "y":
        item = int(input("Enter your item: "))
        if item >= 1 and item <=6:
            if item == 1:
                order_list.append("Pizza")
            elif item == 2:
                order_list.append("Breadsticks")
            elif item == 3:
                order_list.append("Pasta")
            elif item == 4:
                order_list.append("Burger")
            elif item == 5:
                order_list.append("Cake")
            else:
                order_list.append("Chips")
        else:
            print("Invalid selection of Item")
        ch = input("Do you want to continue(y/n): ")
addItems(ch,order_list)
print(order_list)
