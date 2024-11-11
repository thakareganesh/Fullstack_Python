"""
# Task 3: Consider Halltiket numbers are ['112221001','115622053','112221022','185621050','112221029','115622023','116522001']
# Test Case 1:
    Enter collage code: 1122
    your halltickets number: 112221001
                             112221022
                             112221029

# Test Case 2:
    Enter collage code: 1235
    Sorry..! No halltickets are available
"""

hall_tkts = ['112221001','115622053','112221022','185621050','112221029','115622023','116522001']
collage_code = input("Enter collage code: ")
found = False

print("Your halltickets are: ",end="")
for hts in hall_tkts:
    if hts.startswith(collage_code):
        print(hts,end="\t")
        found = True
    if not found:
        print("Sorry..! No halltikcets are avaialable")
        break
