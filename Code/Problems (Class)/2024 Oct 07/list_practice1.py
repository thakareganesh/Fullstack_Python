# Task 1: append()
# Create an empty list and append the numbers from 1 to 5 to it. Print the list after each append operation.

my_list = []
my_list.append(1)
print(my_list)

my_list.append(2)
print(my_list)

my_list.append(3)
print(my_list)

my_list.append(4)
print(my_list)

my_list.append(5)
print(my_list)

print("=" * 30)

#Task 2: insert()
#Take a list of numbers [1, 2, 4, 5]. Use the insert() function to insert the number 3 at the correct
# index to make the list sorted. Print the final list.

lst1 = [1,2,4,5]
lst1.insert(2,3)
print(lst1)

print("=" * 30)

#Task 3: count()
#Take a list ['apple', 'banana', 'apple', 'cherry', 'apple', 'banana'].
#Count how many times 'apple' and 'banana' appear in the list.

lst2 = ['apple', 'banana', 'apple', 'cherry', 'apple', 'banana']
print("Apple:",lst2.count('apple'))
print("Banana:",lst2.count('banana'))
