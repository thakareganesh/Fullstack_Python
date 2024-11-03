num1 = int(input("Enter your number1: "))
num2 = int(input("Enter your number2: "))
num3 = int(input("Enter your number3: "))
if (num1>num2 and num1>num3):
    print(num1,"is the biggest number")
elif (num2>num1 and num2>num2):
    print(num2,"is the biggest number")
else:
    print(num3, "is the biggest number")