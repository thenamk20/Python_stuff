
class Human:

    type = "humnan"
    def __init__(self,name, gender):
        self.gender = gender
        self.name = name

    def move(self):
        print("A human is moving")

    def sleep(self):
        print("A human is sleeping")


class Character(Human):

    type = "anime"

    def __init__(self,name, maho, age, kingdom):
        
        self.name = name
        self.maho = maho
        self.age = age
        self.kingdom = kingdom
    

    def fight(self):
        print(self.name + " use " + self.maho + " attack!")

    def nansaidesuka(self):
        print(self.name + " kun " +str(self.age) + " years old")


class Hero(Human):
    type = "hero"

    def __init__(self, univer, name):
        self.univer = univer
        self.name = name 

    def save_the_world():
        print("Heros are saving this f world!")