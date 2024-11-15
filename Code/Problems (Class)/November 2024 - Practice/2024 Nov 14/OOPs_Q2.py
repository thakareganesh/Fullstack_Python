# Example 2 = OOPS 2

class test:
    def show(self):
        self.a = 20
        print(self.a)
    def display(self):
        b = 30
        c = self.a + b  # --> NameError: 'a' is not defined.
        print(c)

t1 = test()
t1.show()
t1.display()