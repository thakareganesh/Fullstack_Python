# Question 6
class Google:
    def show(self):
        print("Google")
class yahoo(Google):
    def display(self):
        print("Yahoo")
class Mozilla(yahoo,Google):
    def register(self):
        print("Mozilla")
m1 = Mozilla()
m1.register()