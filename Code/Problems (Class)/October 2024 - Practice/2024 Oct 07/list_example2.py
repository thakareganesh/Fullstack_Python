

list = [10,20,30,10,40,50,60,70,10]

print(list)

list.append(80) # append() function adds the provided item in the end of the list
print(list)


list.insert(1,15) # insert() used to add values in the current list based on the index
print(list)

print(15 in list)
print(25 in list) # in provides the given item is available or not in the current list

print(list.count(10)) # count() tells how many occurrences of the given item are present in current list

print(list.index(10)) # index of the first occurrence of the given item

print(list)
# list.extend((90,100,110,120))
list.extend([90,100,110,120])
print(list)

list.extend(range(130,150,10))
print(list)


