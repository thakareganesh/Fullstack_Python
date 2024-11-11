lst = [10,20,30]
print(lst)
lst.append(40)
print(lst)
lst.extend((50,60,70))
print(lst)
lst.extend([80,90,100])
print(lst)

lst.extend(range(110,210,10))
print(lst)