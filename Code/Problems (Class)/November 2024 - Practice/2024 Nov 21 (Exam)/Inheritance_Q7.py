# Question 7

class SBI:
    def show(self):
        print("Services from SBI")
class credit_card(SBI):
    def show(self):
        print("Services From Credit Card")
class ATM(credit_card):
    def show(self):
        print("Services from ATM")

c1 = ATM()
c1.show()