# Q.3) Read product id , product name and product cost then create dictionary

my_dict = {}

pid = int(input("Enter Product ID: "))
pname = input("Enter Product Name: ")
pcost = eval(input("Enter Product Cost: "))

my_dict[pid] = [pname,pcost]
print(f"My dictionary: {my_dict}")