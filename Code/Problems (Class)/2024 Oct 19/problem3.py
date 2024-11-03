"""
Write a program to read 3 subjects marks , then check student is PASS or FAIL, if Pass then only calculate total,
average and grade
avg >=70 --> Grade A
avg between 60-70 --> Grade B
avg between 50-60 --> Grade C
Otherwise --> Grade D
If Fail, then display message as Better luck next time
"""

# Getting marks form student
chem = int(input("Enter your Chemistry marks: "))
bio = int(input("Enter your Biology marks: "))
phy = int(input("Enter your Physics marks: "))

# Checking student is Pass or Fail
if (chem>=35 and bio >= 35 and phy >=35): # --> if True then student pass
    print("Student is PASS")
    total = chem + bio + phy # --> Calculating total marks
    print("Total marks student got:",total)
    avg = total / 3 # --> Calculating Average Score
    print("Average of Student is:",avg)

    # Calculating Grade according to Average
    if (avg >=70):
        print("Grade - A")
    elif (avg>=60 and avg <70):
        print("Grade - B")
    elif (avg>=50 and avg <60):
        print("Grade - C")
    else:
        print("Grade - D")
else:
    print("Student is FAIL")
    print("Better luck next time")