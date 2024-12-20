
# Tuples practice example 1

t1 = (1,2,3,2,5)
print(type(t1))
print(f"tuples: {t1}")
print("=" * 40) # --> used for decoration purpose

# Indexing allowed in tuples due to they are ORDERED
i1 = t1.index(3)
i2 = t1.index(5)
i3 = t1.index(2)
print(f"5 is present at index: {i2}")
print(f"3 is present at index: {i1}")
print(f"2 is present at index: {i3}")

# slicing is possible 
print(f"Return all tuples: {t1[:]}")
print(f"Return all tuples: {t1[::]}")
print(f"Return all tuples in reverse: {t1[::-1]}")
print("=" * 40) # --> used decoration purpose


# Operation
#print(f"Sorting Tuples: {t1.sorted()}") # Not possible

my_tuple = (1,2,3,4,5)
print(f"My tuple: {my_tuple}")
temp_list = list(my_tuple)
print(f"Temporory List: {temp_list}")
print(temp_list.sort()) # --> returns None
sorted_list = temp_list.sort()
print(sorted_list)