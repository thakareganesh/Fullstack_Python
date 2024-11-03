
s = {10,20,30,40}
print(s) # --> {40, 10, 20, 30}
print(type(s)) # --> <class 'int'>

s = {10,20,10,"Ganesh",30,40}
print(s) # --> {20, 40, 10, 'Ganesh', 30}

# print(s[0]) # -->  TypeError: 'set' object is not subscriptable
# print(s[:]) # --> TypeError: 'set' object is not subscriptable

s.add(50) # add() method is applicable for set only. and for lists we use append()
print(s) # --> {50, 20, 40, 10, 'Ganesh', 30}
s.remove(30)
print(s) # --> {50, 20, 40, 'Ganesh', 10}
print(len(s)) # --> 5
s.add(40)
print(s)

print("=" * 30)

s = {} # its by default empty dictionary
print(s)
print(type(s))

s = set()  # for empty set we use set()
print(s)
print(type(s))