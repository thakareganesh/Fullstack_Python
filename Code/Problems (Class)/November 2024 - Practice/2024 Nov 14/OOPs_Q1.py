# Example 1 = OOPS 2
class test:
    @staticmethod
    def show():
        a = 20
        print(20)
    def display(self):
        b = 30
        print(b)

t1 = test() # Ojbect reference created for class test
test.show()  #--> static method is called by classname
t1.display()  #--> instance method is called by object reference    