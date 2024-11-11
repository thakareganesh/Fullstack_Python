# Question 2: Consider lst = [5,15,10,9,22,4]
# --> Now Read an element and then remove that element

lst = [5,15,10,9,22,4,5]

num = int(input("Enter any number: "))
if num in lst:
    lst.remove(num)
    print(f"{num} element is removed from list")
else:
    print(f"{num} is not available in your list")
print(f"Your elements are: {lst}")