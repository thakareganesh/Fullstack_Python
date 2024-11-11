# 2. float() type casting

# 2.1 int --> float
num = 15  # --> integer value is given
print(type(num)) # --> it will return <class 'int'>
number = float(num) # --> here we are doing float() type casting that converts int to flaot
print(number) # --> it will return 15.0 which is float value
print(type(number)) # --> it will return <class 'float'>

print("=" * 30) # --> just using for separator

# example of binary int value and its acceptable
num = 0b1111
print(num)
print(type(num))
number = float(num)
print(number)
print(type(number))


print("=" * 30) # --> just using for separator


# 2.2 complex --> float

# its not allowd and not possible it will give us TypeError
# Example
num = 10 + 20j
print(num)
print(type(num))
# number = float(num) # it will raise TypeError

print("=" * 30) # --> just using for separator


# 2.3 bool --> float
# It's possible becuase while True treated as 1 and False treated as 0
# Example 1
num1 = True
print(num1)
print(type(num1))
number = float(num1)
print(number)
print(type(number))

print("=" * 30) # --> just using for separator

# Example 2
num2 = False
print(num2)
print(type(num2))
number = float(num2)
print(number)
print(type(number))

print("=" * 30) # --> just using for separator

# 2.4 str -> float
# Its is only possible when string internally containst decimal value which should base 10 and no other characters.

# Example 1
num = "100"
print(type(num))
print(num)
number = float(num)
print(type(number))
print(number)

print("=" * 30) # --> just using for separator

# Example 2
num = "0b1111"
print(float(num))