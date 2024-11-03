# Question: Read 3 Subjects marks, now find total and average marks and print it.

total_subjects = 3

chemistry_marks = eval(input("Enter your chemistry subjects marks: "))
physics_marks = eval(input("Enter your physics subjects marks: "))
biology_marks = eval(input("Enter your biology subjects marks: "))

total_marks = chemistry_marks + physics_marks + biology_marks
print("Total marks in 3 subjects:",total_marks)

average_marks = total_marks/total_subjects

print("Average Marks:",average_marks)