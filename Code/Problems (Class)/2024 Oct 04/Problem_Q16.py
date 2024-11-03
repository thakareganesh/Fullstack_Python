"""
Question 16: Mr. Venkat Readdy and his frineds (Vishnu, Avinash) went to restarurant and placed order as 3 plates of manchuriya,
and 2 plates of biryani. They give tip as 20 rs. Now they decided to share amount equally. Write a program to display there sharing
amount . (Note: Manchuriya cost is 220/plate, Biryani Cost is 360/plate)
"""

biryani_price = 360
manchuriya_price = 220
no_of_friends = 3
tip = 20

total_manchuriya = manchuriya_price * 3
total_biryani = biryani_price * 2

total_bill = total_biryani + total_manchuriya + tip
print("Total bill: " , total_bill)

split_amount = total_bill / no_of_friends
print("Each friend have to pay: ", split_amount)