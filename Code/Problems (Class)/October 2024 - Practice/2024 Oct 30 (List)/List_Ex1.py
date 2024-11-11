# Adding elements in list

a1 = []
print("Your elements are:",a1)

# append() method
a1.append(5)
a1.append(9)
a1.append(15)
a1.append(8)
print("Your elements are:",a1)

# insert() method
a1.insert(1,25)
print("Your elements are:",a1)

# instead of extend() if we use append method for another list to adding existing list
a2 = [10,12,18]
a1.append(a2)
print("Your elements are:",a1)

# we use extend()
a3 = [50,60,70]
a1.extend(a3)
print("Your elements are:",a1)

