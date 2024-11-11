

l = [10 ,20, 30, 40]
b = bytearray(l)
print(type(b)) # --> <class 'bytearray'>

print("=" * 30)

print(b[0]) # --> 10
print(b[-1]) # --> 40

b[0] = 77
for x in b:
    print(x)

