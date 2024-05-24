#!/usr/bin/env python3


#  swim
class SwimMixin:
    def swim(self):
        print("The creature swims!")


# FlyMixin  method
class FlyMixin:
    def fly(self):
        print("The creature flies!")


# Dragon class inherit
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")


# Instantiate a Dragon object
draco = Dragon()


# Demonstrate abilities
draco.swim()
draco.fly()
draco.roar()
