
#mutiple inheritance is so complicated

from abc import ABC, abstractmethod  #abstact class


class Animal(ABC):
    def common(self):
        print("Animal")
        return self
    
    @abstractmethod
    def move(self):
        pass

class Prey():
    
    def flee(self):
        print("Fleeing")
        

    def common(self):
        print("Prey")
        super().common()
        return self

    def move(self):
        print("A Prey is moving")

class Predator(Animal):
    def hunt(self):
        print("hunting")
        
    def common(self):
        print("Predator")
        super().common()
        return self
    
    def move(self):
        print("A predator is moving")

#---------------------------

class Fish(Prey, Predator):
    
    def common(self):
        print("Fish")
        super().common()
    
    def move(self):
        print("A fish is swimming.")
        super().move()

fish = Fish()
fish.common()

print(Fish.__mro__)


