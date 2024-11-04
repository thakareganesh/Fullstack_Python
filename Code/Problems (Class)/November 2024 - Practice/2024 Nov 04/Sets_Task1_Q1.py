# Sets Task 1:
# Consider following sets

Jubilee_Hills = {"Allen Solly", "Wrangler", "Pepe Jeans", "Levi's", "Flying Machine", "Allen Solly", "Spykar", "VanVeusen"}
BegumPet = {"Allen Solly", "Mufti", "Wrangler", "Pepe Jeans", "Lee", "Van Heusen", "Monte Carlo", "Flying Machine"}
print(f"Jubilee Hills: {Jubilee_Hills}")
print(f"BegumPet: {BegumPet}")

print("=" * 120)
# Question 1: Display the common brands available in two places
common_brands = Jubilee_Hills.intersection(BegumPet)
print(f"These are the following brands which are common: {common_brands}")

print("=" * 120)
# Question 2: Display the brands which are available only in BegumPet Branch
only_BegumPet = BegumPet.difference(Jubilee_Hills)
print(f"These are the brands which are only available in BegumPet: {only_BegumPet}")

print("=" * 120)
# Question 3: Display the unique brands available in jubilee hills and begumpet branch
both_unique = Jubilee_Hills.symmetric_difference(BegumPet)
print(f"These are the brands which are unique in both Jubilee Hills and Begumpet: ")
print(both_unique)