"""
Question 33: Read Employee annual salary and hike percentage, then calculate annual salary after hike.
And display new monthly salary
"""
months_in_year = 12
annual_salary = float(input("Enter your annual salary: "))

hike_percentage = float(input("How much hike you got, Enter in percentage: "))

hike_increment = annual_salary * hike_percentage / 100
print("Total hike increment got: ",hike_increment)

final_annual_salary = annual_salary + hike_increment
print("Annual salary after hike: ",final_annual_salary)

monthly_salary = final_annual_salary / months_in_year
print("Monthly salary after hike: ",monthly_salary)