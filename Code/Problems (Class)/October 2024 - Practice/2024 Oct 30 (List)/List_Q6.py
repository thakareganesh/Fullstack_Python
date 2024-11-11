# Question 6: Consider customer order is ["idly","vada","puri"]
# --> Now read an item if available then delete that item
# --> Enter item name: vada             |   Enter item name: pongal
#     vada is deleted from your order   |   Sorry..! Your item pongal is not available in your list
#     your final order is: ["idly","puri"]    |   your final order is: ["idly","vada","puri"]

order_list = ["idly","vada","puri"]
print("Orignal order list:",order_list)
item = input("Enter item name to remove: ")

if item in order_list:
    order_list.remove(item)
    print(f"{item} is deleted from your order")
else:
    print(f"Sorry..! Your item {item} is not available in your list")

print(f"Your final order is: {order_list}")