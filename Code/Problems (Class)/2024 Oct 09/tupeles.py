

t = (10, 20, 30, 10, "Ganesh")

print(type(t)) # --> <class 'tuple'>
print(t) # --> (10, 20, 30, 10, 'Ganesh')

print(t[0]) # --> 10
print(t[-1]) # --> Ganesh
print(t[4]) # --> Ganesh
print(t[1:4]) # --> (20, 30, 10)
print(t[0:(len(t))]) # --> (10, 20, 30, 10, 'Ganesh')

# t[0] = 7777 # --> TypeError: 'tuple' object does not support item assignment

# t.extend[10] # --> AttributeError: 'tuple' object has no attribute 'extend'


