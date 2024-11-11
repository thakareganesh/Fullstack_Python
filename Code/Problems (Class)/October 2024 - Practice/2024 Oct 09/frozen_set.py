

# SET Operation and representation
s = {10,20,30,40}
print(s) # --> It's set and it will return: {40, 10, 20, 30}
print(type(s)) # --> <class 'set'>

s.add(50)
print(s) # --> {40, 10, 50, 20, 30}
s.remove(30)
print(s) # --> {40, 10, 50, 20}

print("=" * 30)

# Frozen SET operation and representation

s = { 10,20,30,"Ganesh",50}
fs = frozenset(s)
print(fs) # --> frozenset({'Ganesh', 50, 20, 10, 30})
print(type(fs))  # --> <class 'frozenset'>

# fs.add(50) # --> AttributeError: 'frozenset' object has no attribute 'add'
fs.remove(30) # --> AttributeError: 'frozenset' object has no attribute 'remove'