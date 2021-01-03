from abc import ABC, abstractmethod
import sys



class Fighter:
    def __init__(self):
        self.obj=None

    def setter(self, obj=None):
        self.obj=obj

    def getter(self):
        self.obj

    def use_Object(self):
        self.obj.use_me()


class Abstract_Fight(ABC):
    @abstractmethod
    def use_me(self):pass
    #nothing goes here

class Concrete_Shoot():
    def __init__(self): pass

    def use_me(self):
        print("I shoot people")

class Concrete_RailGun_Shooting():
    def __init__(self): pass

    def use_me(self):
        print("I shoot planes between the fuselage")

fighter1=Fighter()
fighter3=Fighter()

fight_method1=Concrete_Shoot()
fight_method3=Concrete_RailGun_Shooting()

fighter1.setter(fight_method1)
fighter3.setter(fight_method3)


fighter1.use_Object(); fighter3.use_Object()