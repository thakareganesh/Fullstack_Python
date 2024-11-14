# Dommino's Pizza Hut Project

menu  = """\tDominos Pizza Hut
    M E N U  C A R D
    1. Pizza
    2. Breadsticks
    3. Pasta
    4. Burger
    5. Cake
    6. Chips"""
print(menu)

ch = "y"
order_list = []


# Order Selection
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
print("Your order is:",order_list)
print("=" * 40)


# Order Modification
mod = input("Do you want to modify order(y/n): ")
if mod == "y":
    print("""\t1. Add Item
    2. Delete Item
    3. Modify Item""")
    ch1 = int(input("Enter your choice: "))

    # Add Item
    if ch1 >= 1 and ch1 <=3:
        if ch1 == 1:
            print(menu)
            add_ch = "y"
            while add_ch == "y":
                new_item = int(input("Enter your choice: "))
                if new_item > 0 and new_item < 7:
                    if new_item == 1:
                        order_list.append("Pizza")
                    elif new_item == 2:
                        order_list.append("Breadsticks")
                    elif new_item == 3:
                        order_list.append("Pasta")
                    elif new_item == 4:
                        order_list.append("Burger")
                    elif new_item == 5:
                        order_list.append("Cake")
                    else:
                        order_list.append("Chips")
                else:
                    print("Invalid selection of choice")
                add_ch = input("Do you want to continue(y/n): ")
            #print("Your order is:",order_list)
            print("=" * 40)

        # Remove Item
        elif ch1 == 2:
            del_ch = "y"
            while del_ch=="y":
                rem_item = input("Enter the item name to delete from the list: ")
                if rem_item in order_list:
                    order_list.remove(rem_item)
                    print(f"{rem_item} is deleted from order list")
                else:
                    print(f"{rem_item} is not available in order list")

                del_ch = input("Do you want to continue(y/n): ")
            #print(f"Your order is: {order_list}")
            print("=" * 40)

        # Modify items
        else:
            print(f"Your order is: {order_list}")
            change_ch = "y"
            while change_ch == "y":
                mod_item = input("Enter item name to modify: ")
                replace_item = input("Enter item to replace: ")
                if mod_item in order_list and replace_item not in order_list:
                    index = order_list.index(mod_item)
                    order_list[index] = replace_item
                    print(f"Your order is updated,Your choice {mod_item} is replaced with {replace_item}")
                elif mod_item == replace_item:
                    print(f"You want to replace item {mod_item} with {replace_item}, Both are same ")
                else:
                    print(f"Sorry..! {mod_item} is not available in order list")
                change_ch = input("Do you want to continue(y/n): ")
    else:
        print("Invalid selection of Modification")
print(f"Your order is: {order_list}")