# OOPs-2 : Example 4

class Test:
    def show(self):
        self.a = 20
        print(self.a)
    def display(self):
        b = 30
        c = self.a - b
        print(c)

a1 = Test()
a1.display()
a1.show()