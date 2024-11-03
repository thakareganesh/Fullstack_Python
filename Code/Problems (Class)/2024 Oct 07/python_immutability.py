# Python Variable Reusability and immutability checking

# Integer datatype
int_num1 = 100
int_num2 = 100
int_num3 = 100
print("Integer number 1:",id(int_num1))
print("Integer number 2:",id(int_num2))
print("Integer number 3:",id(int_num3))
print(int_num1 is int_num2) # --> True. We can reuse variable values with same memory allocation

print("=" * 30)

# Float Datatype
float_num1 = 100.50
float_num2 = 100.50
print("Floating number 1:",id(float_num1))
print("Floating number 2:",id(float_num2))
print(float_num1 is float_num2) # --> True. We can reuse variable values with same memory allocation

print("=" * 30)

# Boolean Datatypes
bool_val1 = True
bool_val2 = True
print("Boolean Value 1:",id(bool_val1))
print("Boolean Value 2:",id(bool_val2))
print(bool_val1 is bool_val2)

print("=" * 30)

# Complex Datatypes
complex_val1 = 10 + 20j
complex_val2 = 10 + 20j
print("Complex Value 1:",id(complex_val1))
print("Complex Value 2:",id(complex_val2))
print(complex_val1 is complex_val2)