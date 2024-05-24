#!/user/bin/env pytho3
"""abstract class"""

from abc import ABS, abstractmethod


# abstract mainclass
class Animal(ABS):

    @abstractmethod
    def sound(self):
        pass


# subclass inherts form the animal
class Dog(Animal):

    def sound(self):
        return "Bark"


# subclass inherts from the animal
class cat(Animal):
    def sound(self):
        return "Meow"
