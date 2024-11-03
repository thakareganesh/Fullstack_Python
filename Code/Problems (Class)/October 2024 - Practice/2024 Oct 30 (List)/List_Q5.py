# Question 5: Consider customer order is ["idaly","vada","puri"]
"""
--> Enter item name to modify: idaly                | Enter item name to modify: dosa
    idaly is available in index number: 0           | Sorry..! your item dosa is not available in your list
    Enter new item for replace current item: dosa   |
    Your final order is: ["dosa","vada","puri"]     |
"""

cust_order = ["idaly","vada","puri"]
print("Your order is:",cust_order)

item= input("Enter item name to modify: ")

if item in cust_order:
    i = cust_order.index(item)
    print(f"{item} is available in index number: {i}")
    new_item = input("Enter new item for replace current item: ")
    cust_order[i] = new_item

else:
    print(f"Sorry..! Your item {item} is not available in your list")

print("Your final order is:",cust_order)