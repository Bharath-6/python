#OOP in python
""" TO map with real world scenarious, we started using objects in code.
This is called object oriented programming"""

#class & Object in python

""" Class is blueprint for creating objects.
class Student:
    name = "Karan kumar"

#creating object(instance)
s1 = Student()
print(s1.name)"""

"""
#creating class
class Student:
    name = "karan"
#creating object(instance)
s1 = Student()
print(s1.name) #karan

s2 = Student()
print(s2.name)#karan

class Car:
    color = "blue"
    model = "v4"
    brand = "Audi"
car1 = Car()
print(car1.color)
print(car1.brand)"""

#Constructor __init__ Function
# All classes have a function called __init__(), which is always executed when the class is being initiated.
#if we use __init__ or not then always their will be constructor

#constructor always takes The self parameter is a reference to the current instance of the class, and it used to access variables that belongs to the class
#creating class
class Student:
    college_name = "Gitam University" #Class & Instance Attribute
    def __init__(self,name,marks): #self is a reference of the object ex: student
        self.name = name #obj attr
        self.marks = marks
        print("adding new student in Database...")
#creating object
s1 = Student("Bharath",22) # the bracket after student is used to call the constructor
print(s1.name,s1.marks)
print(Student.college_name) ##Class & Instance Attribute this we are utilizing from above

s2 = Student("arjun",44)#The data which we are storing is known as attributes
print(s2.name,s2.marks)
print(Student.college_name)

#if we have same class attr name and same obj attr name then obj> class att

#Class & Instance Attributes
#we will give in student class not in the constructor where it will be applicable for all object
# Class.attr
# Obj.attr


#default constructors
"""def __intit__(self):
    print("adding ")
    pass            
"""
#parameterized constructors
"""def __init__(self,name,marks): #self is a reference of the object ex: student
        self.name = name
        self.marks = marks
        print("adding new student in Database...")"""