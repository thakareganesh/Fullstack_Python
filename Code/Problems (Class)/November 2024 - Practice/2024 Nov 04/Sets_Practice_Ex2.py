# Sets Function Practice

# Initalizing empty set
s1 = set()
print(f"Empty Set 1: {s1}")
s2 = set({})
print(f"Empty Set 2: {s2}")


# Consider set as S3
s3 = { 1,5,9,10,1,5,10,7,50,30,41,50,0,-5}
print(f"Set 3: {s3}") # --> printing set with unique elements

# Sum() in sets
sum = sum(s3)
print(f"The sum of all elements in sets is: {sum}")

# min() in sets
min = min(s3)
print(f"Minimum Value in current set 3: {min}")

# max() in sets
max = max(s3)
print(f"Maximum Value in current set 3: {max}")

# len() in sets
lenth = len(s3)
print(f"Number of elements in current set 3: {lenth}")

# sorted() in sets
sort = sorted(s3)
print(f"Set 3 in aceding order: {sort}")