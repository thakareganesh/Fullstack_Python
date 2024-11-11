"""
# Task 3: Consider Hall-ticket numbers are ['112221001','115622053','112221022','185621050','112221029','115622023','116522001']
# Test Case 1:
    Enter collage code: 1122
    your hall-tickets number: 112221001
                             112221022
                             112221029

# Test Case 2:
    Enter collage code: 1235
    Sorry..! No hall-tickets are available
"""
halltkts = ['112221001','115622053','112221022','185621050','112221029','115622023','116522001']
clg_code = int(input("Enter collage code: "))
found = False
print("Your hall-tickets number: ",end=" ")
for hts in halltkts:
    if hts.startswith(str(clg_code)):
        print(hts,end="\t")
        found = True
if not found:
    print("Sorry..! No hall-tickets are available")