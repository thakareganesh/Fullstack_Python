

d = { 100:"Ganesh",
      200:"Shubham",
      300:"True",
      400: 105,
      500: 105.50
      }
print(d)
print(type(d))

print("=" * 30)

d2 = {}
print(d2)
print(type(d))
d2[100] = "Ganesh"
print(d2)
d2[200] = "Shubham"
print(d2)

print("=" * 30)

d = {100:"Ganesh",200:"Shubh"}
print(d) # --> {100: 'Ganesh', 200: 'Shubh'}
d[100] = "Akash"
print(d) # --> {100: 'Akash', 200: 'Shubh'}
d[300] = "Akash"
print(d) # --> {100: 'Akash', 200: 'Shubh', 300: 'Akash'}