# Task 5: Consider a = (3,7,2,15), Now add "9" to your tuple

a = (3,7,2,15)  # its tuple
a = list(a) # converting to list
a.append(9) # appending '9' to converted list
a = tuple(a) # again converted back to tuple
print(f"Our tuple: {a}") # printed tuple