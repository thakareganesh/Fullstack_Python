

r = range(10)
print(type(r))
print(r)

for x in r:
    print(x)

print("=" * 33)

# Another Example
r = range(1,10)
for x in r:
    print(x)

# Another Example
r = range(5,10)
for x in r:
    print(x)

print("=" * 30)
# Form 3 : r = range(1 , 21, 1)
r = range(1,21,2)
for x in r:
    print(x)
print("=" * 30)

r = range(1,11,2)
for x in r:
    print(x)

print("=" * 30)
r = range(1,11,3)
for x in r:
    print(x)

print("=" * 30)

# Another example with decrement step
r = range(20,1,-5)
for x in r:
    print(x)

print("=" * 30)


# Indexing and Slicing with the range datatypes
r = range(10,21) # 10,11,12,13.......,20
# indexing
print(r[0]) # --> 10
print(r[-1]) # --> 20

# slicing
r1 = r[1:5]
print(r1) # --> range(11,15)
for x in r1:
    print(x) # --> 11,12,13,14

# checking immutability
print(r) # --> range(10,21)
print(r[1]) # --> 11
r[1] = 1000 # --> TypeError: 'range' object does not support item assignment

