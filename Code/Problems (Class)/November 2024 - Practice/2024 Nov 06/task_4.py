# consider  a = [5,9,12,15,4] Now read an element from user, in ase that element available then modify that element with
# new element

a = [5,9,12,15,4]

ele1 = int(input("Enter your element: "))
for i in a:
    if ele1 == i:
        print(f"Your element {ele1} is  available in our list")
        ele2 = int(input("Enter Your value to replace: "))
        index = a.index(ele1)
        a[index] = ele2
        break
else:
    print(f"Your element {ele1} is not available in our list")

print("Your record are:",a)