class user:
    def sign_in(self):
        print('logged in')

class Wizard(user):
    def __init__(self,name,power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(user):
    def __init__(self,name,num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left -  {self.num_arrows}')

wizard1 = Wizard('Merlin',50)
Archer1 = Archer('Robin',100)
wizard1.attack()
print(Archer1.sign_in())