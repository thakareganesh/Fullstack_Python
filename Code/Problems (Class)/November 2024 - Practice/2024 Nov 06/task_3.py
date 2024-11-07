

a = [5,9,12,15,4]

n = int(input("Enter any number: "))

for i in a:
    if n == i:
        print("Available")
        break
else:
    print("Not avaialable")

# if n in a:
#     print("Available")
# else:
#     print("Not avaialable")
