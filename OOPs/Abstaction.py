#Abstraction
# Hiding the implementation details of a class the only showing the essential features to the user.
"""four pillars of oops
1)Abstraction
2)Encapsulation
3)Polymorphism
4)Inheritance"""
class Car:
    def __init__(self):
        self.accelerator = False
        self.brk = False
        self.clutch = False
    def start(self):
        self.clutch = True # this are unneccessary implenting things we are not showing just printing car started this is know ans abstraction
        self.acc = True
        print("car Started.")
car1 = Car()
car1.start()