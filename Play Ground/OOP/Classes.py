class Profile():
    def __init__(self):
        self.name = "bob"
    def SayHi(self, _name):
        print(f"Hi {_name}")

profile1 = Profile()

print(profile1.name)

profile1.SayHi("bob")
print(profile1.name)