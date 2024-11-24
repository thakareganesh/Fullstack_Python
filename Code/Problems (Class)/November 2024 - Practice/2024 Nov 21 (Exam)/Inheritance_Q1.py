class google:
    def show(self):
        print("Google")
class yahoo(google):
    def display(self):
        print('Yahoo')
class Mozilla(yahoo):
    def register(self):
        print("Mozilla")

m1 = Mozilla()
m1.register()
m1.display()
m1.show()