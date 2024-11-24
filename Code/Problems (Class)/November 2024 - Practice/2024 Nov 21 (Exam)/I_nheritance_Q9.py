# Question 9

class SBI:
    def __init__(self):
        print("Services from SBI")
class credit_card(SBI):
    def _init__(self):
        print("Services From Credit Card")
class ATM(credit_card):
    def _init__(self):
        print("Services from ATM")
c1 = ATM()
c1.credit_card()