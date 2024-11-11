#   

num = int(input("Enter any number: "))
end = int(input("Enter table upto: "))
for i in range(1, end+1):
    table = num * i
    print(num, "*", i, "=", table)
