#Class Method
""" A class method is bound to the class & receives the class as an implicit first argument.

Note - static method can't access or modify class state & generally for utility."""
#we need to change the class attribute
# class  Person:
#     name = "anonymous"

#     def changeName(self,name):
#         self.name = name

# p1 = Person()
# p1.changeName("Bharath") #Bharath
# print(p1.name)
# print(Person.name)#anonymous

#using class method we can change direct class attribute
class  Person:
    name = "anonymous"

    @classmethod
    def changeName(cls,name):
        cls.name = name

p1 = Person()
p1.changeName("Bharath") #Bharath
print(p1.name)
print(Person.name)#Bharath

#Types of Methods:
"""
1)static methods
2)class Methods(class)
3)instace methods(self) """

#Property Decorator
# we use @property decorator on any method in teh class to use the method as property
class Student:
    def  __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math

    # def calPercentage(self):
    #     self.percentage = str((self.phy+self.chem+self.math)/3) +"%"
    #insteaded of above we use
      
      # in property method what ever the change out of the class we do it will automatically reflect here
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3) + "%"

stu1 = Student(98,97,96)
print(stu1.percentage)#97.0%


#if the teacher want to change the marks of 97 to 85 she can change 
#stu1.phy = 85
# But the marks will change but the percentage wont change becuase it was seted with previous values
#now we used property method
stu1.phy = 85
print(stu1.percentage)#92.66666666666667%
#Now it changed