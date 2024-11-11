l1 = [10,20,30,40]
print(id(l1))
print(l1)

l2 = l1
print(id(2))
print(l2)

l1[3] = 400
print(l1)

print(l2)

l2[0] = 100

print(l1)
print(l2)