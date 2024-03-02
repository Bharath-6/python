#Inheritance
""" when one class(child/derived) derives the properties & methods of another class(parent/base). """
# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("car started..")
    
#     @staticmethod
#     def stop():
#         print("car stopped.")
# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name = name

# car1 = ToyotaCar("fortuner")
# car2 = ToyotaCar("prius")

# print(car1.start())
# print(car1.color)

#Types
"""
1)Single Inheritance
#base --> Derived (child class)
2)Multi-level Inheritance
#base --> Derived (child class) --> Derived(Child)
3)Multiple Inheritance """

#Multi-Level Inheritance
# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("car started..")
    
#     @staticmethod
#     def stop():
#         print("car stopped.")
# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name = name

# class Fortuner(ToyotaCar): #fortuner is taking all the properties of Toyota car
#     def __init__(self, type):
#         self.type = type

# c1 = Fortuner("diesel")
# car1.start()


#Multiple inheritance

# Base1 and Base2

# derived - child from both base1 and base2

class A:
    varA = "welcome to class A"
class B:
    varB = "welcome to class B"
class C(A,B):
    varC = "Welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

#Super Method
#Super() method is used to access methods of the parent class.
class Car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped.")
class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type) #we are accessing parent method
        self.name = name
        super().start()
car1 = ToyotaCar("pirus","electric")
print(car1.type)