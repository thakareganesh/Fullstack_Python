# Question 8

class SBI:
    def show(self):
        print("Services from SBI")
class credit_card(SBI):
    def show(self):
        print("Services From Credit Card")
class ATM(credit_card,SBI):
    def show(self):
        print("Services from ATM")

c1 = ATM()
c1.show()