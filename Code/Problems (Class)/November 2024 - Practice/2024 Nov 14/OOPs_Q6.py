# OOPs - 2: Example 6

class RBI:
    def assing(self):
        self.a = 20000
        self.b = 30000
    def deposit(self):
        self.c = self.a + self.b
        print(self.c)
    def withdraw(self):
        d = self.c - self.a
        print(d)

rbi1 = RBI()
rbi1.assing()
rbi1.deposit()
rbi1.withdraw()