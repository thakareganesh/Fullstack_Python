# Input: Marks for the three subjects
subject1 = int(input("Enter marks for Subject 1: "))
subject2 = int(input("Enter marks for Subject 2: "))
subject3 = int(input("Enter marks for Subject 3: "))

# Initialize pass count
pass_count = 0

# Check each subject to see if Avinash passed
if subject1 >= 32:
    pass_count = pass_count + 1  # Increment by 1 if he passes
if subject2 >= 32:
    pass_count = pass_count + 1  # Increment by 1 if he passes
if subject3 >= 32:
    pass_count = pass_count + 1  # Increment by 1 if he passes

# Determine if Avinash passed based on the pass_count
if pass_count >= 2:  # He needs at least 2 subjects to pass
    print("Avinash has cleared at least 2 subjects, so he passed.")
else:
    print("Avinash failed to clear at least 2 subjects, so he did not pass.")
