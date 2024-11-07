# Sets Task 1:


print("Brand Factory")
print()
# taking empty set 1 for Jubilee Hills branch
jubilee_hills = set()
# Adding values in jubilee hills
jubilee_hills.add("Allen Solly")
jubilee_hills.add("Wrangler")
jubilee_hills.add("Pepe Jeans")
jubilee_hills.add("Levi's")
jubilee_hills.add("Flying Machine")
jubilee_hills.add("Allen Solly")
jubilee_hills.add("Spykar")
jubilee_hills.add("VanVeusen")
print(f"Jubilee Hills Brands: {jubilee_hills}")
print()
# taking empty set 2 for BegumPet branch
begumPet = set()
begumPet.add("Allen Solly")
begumPet.add("Mufti")
begumPet.add("Wrangler")
begumPet.add("Pepe Jeans")
begumPet.add("Lee")
begumPet.add("Van Heusen")
begumPet.add("Monte Carlo")
begumPet.add("Flying Machine")
print(f"BegumPet Brands: {begumPet}")
print()
# Q.1) Display the common brands available in two places
common_brands = jubilee_hills.intersection(begumPet)
print(f"Following are the Brands which are common brands available in both place: \n{common_brands}")
print()

# Q.2) Display the brands which are available only in Begumpet branch
only_BegumPet = begumPet.difference(jubilee_hills)
print(f"Follwing are the brands which are only available in BegumPet: {only_BegumPet}")
print()

# Q.3) Display the unique brands which are available in Jubilee Hills and BegumPet Branch.
unique_in_both = begumPet.symmetric_difference(jubilee_hills)
print("Following are the brands which are available in Jubilee Hills and BegumPet Branch except common:")
print(unique_in_both)
print()