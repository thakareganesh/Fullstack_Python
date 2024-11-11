# Sets Task 2: Take 2 sets, then perform following operations.
"""
            Team A          Team B
           --------        --------
            Venkat          Srinu
            Vishnu          Lakshmi
            Sarma           Venkat
            Pavana          Sarma
            Leena           Ravali
"""
branch_A = {"Venkat", "Vishnu", "Sarma", "Pavana", "Leena"}
branch_B = {"Srinu", "Lakshmi", "Venkat", "Sarma", "Ravali"}
print(f"Employees of Team A: {branch_A}")
print(f"Employees of Team B: {branch_B}")
print("=" * 120)

# Question 1:  Now find how many Employees are working
branch_OG = branch_A.union(branch_B)
print(f"Orignal Team: {branch_OG}")
emp = len(branch_OG)
print(f"Currently {emp} employees are working on both Branches")
print("=" * 120)

# Question 2: Display the employee names who are working in both branches
both_branch = branch_A.intersection(branch_B)
print(f"These are the employee names who are working in both branches: {both_branch}")
print("=" * 120)

# Question 3: Display the employee name who are working only in branch B
print(f"following are the employee names who are working only in Branch B: {branch_B}")

# Question 4: Display the employee name who are working only in branch B except common employee
only_branch_B = branch_B.difference(branch_A)
print(f"following are the employee name who are working only in branch B except common employee: {only_branch_B}")
print("=" * 120)

# Question 5: Display all employees except common employee names
except_common = branch_A.symmetric_difference(branch_B)
print(f"Following are all employees except common employee names: {except_common}")