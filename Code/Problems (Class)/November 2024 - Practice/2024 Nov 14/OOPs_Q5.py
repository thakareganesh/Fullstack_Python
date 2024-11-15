# OOPs-2: Example 5

class RBI:
    def assign(self):
        self.a = 20000
        self.b = 30000
    # def operations(self):
    #     c = self.a + self.b
    #     print(c)
    def operations(self):
        self.c = self.a + self.b
        print(self.c)
rbi = RBI()
rbi.assign()
rbi.operations()