# Question 3:

class Google:
    def Hr(self):
        self.a = 2
        print(self.a)

class Yahoo(Google):
    def Developer(self):
        super().Hr()
        self.b = 4
        print(self.b)
class Mozilla(Yahoo):
    def __init__(self):
        super().Developer()
        c = self.a + self.b
        print(c)
m1 = Mozilla()
m1.Developer()
m1.Hr()