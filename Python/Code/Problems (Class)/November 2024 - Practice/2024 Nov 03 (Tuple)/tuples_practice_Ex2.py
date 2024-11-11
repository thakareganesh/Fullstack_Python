# Adding elements in tuples

t1 = ('CSE',"IT",'ECE')
print(f"Your courses are: {t1}")

t1 = list(t1)
print(f"temporory list: {t1}")

t1.append("EEE")
t1 = tuple(t1)

print(f"Your courses are: {t1}")