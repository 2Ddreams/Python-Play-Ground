class Enemy():
    def __init__(self, name="Enemy Default Name", hp=None, atk=None):
        self.name = f"NAME: {name}"
        self.hp = f"HP: {hp}"
        self.atk = f"ATK: {atk}"
    


 


Enemy1 = Enemy("BOB", 10, 5)

print(Enemy1.name)
print(Enemy1.hp)
print(Enemy1.atk)

