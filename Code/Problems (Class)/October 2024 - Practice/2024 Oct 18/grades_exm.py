
chem = int(input("Enter your chemistry marks: "))
phy = int(input("Enter your physics marks: "))
bio = int(input("Enter your biology marks: "))

total_marks = chem + phy + bio
no_of_subjects = 3
average = total_marks / no_of_subjects
print("Your total marks is: ",total_marks)
print("Your average is: ", average)
if (average>90):
    grade = "A"
elif (average>= 70 and average <=80):
    grade = "B"
elif (average>=50 and average <70):
    grade = "C"
else:
    grade = "D"

print("Your grade is:",grade)