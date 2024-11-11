# Type Casting Examples and Practice


# 1. int() type casting
# Example 1.1. Float to Int type casting

num = 10.514 # ---> Float type values given 
print(type(num)) # it will return <class 'float'>
number = int(num) # ---> here we use type int() for type casting
print(number) # it will only return 10
print(type(number)) # it will return <class 'int'>


print("=" * 30) # for reference for understanding and using for separator

# Example 1.2. Complex to Int Type Casting
num = 10 + 20j # --> complex type of value is given
print(type(num)) # it will return <class 'complex'>
# number = int(num) # it will raise TypeError
# print(number)
# print(type(number))


print("=" * 30) # for reference for understanding and using for separator

# Example 1.3. Bool to Int type casting
num = True # --> here boolean value True is provided its act as 1
print(type(num)) # --> it will return <class 'bool'>
num2 = False # --> here boolean value True is provided its act as 0
print(type(num2)) # --> it will return <class 'bool'>
number = int(num) * int(num2) # here we use int() for typecasting that converts True = 1 and False = 0 it becomes 1 * 0
print(number) # --> it will return 0 becuase (True * False) = False which means 1 * 0 = 0
print(type(number)) # --> it will return <class 'int'>


print("=" * 30) # for reference for understanding and using for separator

# Example 1.4 Str to int type of casting
num = "15" # --> here string value in decimal (base 10) form is given as "15"
print(type(num)) # --> it will return <class 'str'>
number = int(num) # --> here we used int() for typecasting that converts string value which is in decimal form into integer
print(type(number)) # --> it will return <class 'int'>
print(number) # --> it will return 15 as integer.

print("=" * 30) # for reference for understanding and using for separator

num = "0B1111" # --> here binary value is given as a string
print(type(num)) # --> it will return <class 'str'>
print(num) # --> it will return 0B1111 as a string
# number = int(num) #--> it will raise ValueError

print("=" * 30) # for reference for understanding and using for separator

num = "1.5" # here are float value is given as a string
print(type(num)) # it will return <class 'str'>
print(num) # --> it will return 1.5 as a string
# number = int(num) # --> it will raise ValueError

print("=" * 30) # for reference for understanding and using for separator

