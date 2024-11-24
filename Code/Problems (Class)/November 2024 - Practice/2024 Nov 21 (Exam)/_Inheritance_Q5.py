# Question 5

class Google:
    def Hr(self):
        self.a = 2
        print(self.a)
class Yahoo(Google):
    super().Hr()
    def Developer(self):
        self.b = 4
        print(self.b)
class Mozilla(Yahoo):
    super().Developer()
    def __init__(self):
        c = self.a + self.b 
        print(c)
m1 = Mozilla()