# Question 3: lst = [5,15,10,9,22,4]
# Now read a number, if it is available then modify that number with new element otherwise add that element to our list

lst = [5,15,10,9,22,4]
print("Your elements are:",lst)
num = int(input("Enter any element: "))

if num in lst:
    new_val = int(input("Enter new element: "))
    i = lst.index(num)
    lst[i] = new_val
    print(f"Your element {(num)} is updated")
else:
    lst.append(num)
    print(f"Your element {(num)} is added to List")

print("Your elements are:",lst)