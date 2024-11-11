
l = [10,20,30,40,255] # --> its list named l variable.
print(l)
print(type(l))

b = bytes(l) # --> here we converted list into bytes
print(type(b))

for x in b:
    print(x)
