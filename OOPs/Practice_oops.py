#question: Define a circle class to create a circle with readius r using the constructor.
#Define an Area() method of the class which calculates the area of circle.
#Define a perimeter() method of the class which allows you to calculate the perimeter of the circle

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return (22/7)*self.radius ** 2
    def perimeter(self):
        return 2 * (22/7) * self.radius
    

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())


#Question: Define a Employee class with attributes role, department % salary. This class also have show details method.
#create an Engineer class that inherits properties from Employee & has additional attributes: name & age.

class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    def showDetails(self):
        print("role=", self.role)
        print("dept = ",self.dept)
        print("salary =",self.salary)
#inheriting the employee by engineer
class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","75,000")

eng1 = Engineer("Elon Musk", 40)
eng1.showDetails()

#Question: create a class called order which stores item & its price.

""" Use Dunder function __gt__() to convey that:
    order1>order2 if price of order1>price of order 2"""
class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,odr2):
        return self.price>odr2.price

odr1 = Order("chips",25)
odr2 = Order("Tea",8)
print(odr1>odr2) #true