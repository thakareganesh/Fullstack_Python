# Question 4:

class Google:
    def Hr(self):
        a = 2
        print(a)
class Yahoo(Google):
    def Developer(self):
        super().Hr()
        b = 4
        print(b)
class Mozilaa(Yahoo):
    def __init__(self):
        super().Developer()
        c = a + b 
        print(c)
m1 = Mozilaa()