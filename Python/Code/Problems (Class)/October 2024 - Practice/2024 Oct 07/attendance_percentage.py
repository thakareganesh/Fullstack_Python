"""
Question: Consider total number of working days in a collage is 160 days, Read no. of days the student went to college,
Now find his attendance percentage.
"""

working_days = 160
present_days = int(input("How many days did the student go to college: "))

attendance_percentage = (present_days/working_days) * 100
print("Attendance Percentage:",attendance_percentage)