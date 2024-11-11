# a = "abcdefghijklmnopqrstuvwxyz"
# print(len(a))
# ab = a[21:26]
# print(ab)
# print("="*24)


# # testing default values for starting and ending index
# str = "abcdefghijklmnopqrstuvwxyz"
# print(len(str))
# st = str[:6] # testing default beggining value
# print(st)
# st = str[21:] # Testing default of ending index
# print(st)
# str3 = str[:]
# print(str3)
# print(str)
# print("="*24)


# str4 = str[3:1000] # never going to raise index error. 
# print(str4)
# str5= str[5:1] # Empty string we will get
# print(str5)
# print("=" * 24)

# str = "ganesh"
# my_str = str[0].upper() + str[1:5] + str[5].upper()
# print(my_str) #Output: GanesH


# payal ---> payaL
str = "payal"
# my_str = str[0:4] + str[4].upper() # Insted of this we can write below code 👇
my_str = str[0:len(str) - 1] + str[-1].upper()
print(my_str) # O/P: payaL

# ganesh ----> GanesH
str = "ganesh"
my_str = str[0].upper() + str[1:5] + str[5].upper() # 1st Method
my_str1 = str[0].upper() + str[1:len(str) - 1] + str[-1].upper() #2nd Method
print(my_str) # output: GanesH
print(my_str1) # output: GanesH




