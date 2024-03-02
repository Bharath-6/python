#Polymorphisam : operator Overloading
""" when the same operator is allowed to have different meaning according to the context.

Operators & Dunder Funtions
a+b #addition                       a.__add__(b)
a-b #subtraction                    a.__sub__(b)
a*b #multiplication                 a.__mul__(b)
a/b #division                       a.__truediv__(b)
a%b #finding remainder              a.__mod__(b)        """ 


#This all are implicit overloading
print(1+2) #3
print("apna"+"college") #concatenate
print([1,2,3]+[4,5,6]) #merge
#for numbers it doing one thing for string it is doing another thing it known as Operator overloading

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def showNumber(self):
        print(self.real,"i+",self.img,"j")
    
    def __add__(self,num2):
        newReal = self.real+num2.real
        newImg = self.img+num2.img
        return Complex(newReal,newImg)

num1 = Complex(1,3)
num1.showNumber()#1 i+ 3 j

num2 = Complex(2,7)
num2.showNumber()#2 i+ 7 j

# num3 = num1.add(num2)
# num3.showNumber() #3 i+ 10 j #it also works
#we get error
"""num3 = num1+num2
num3.showNumber()"""
#if we use dunder function __ add__ then it will work
num3 = num1+num2
num3.showNumber()
#where works for different operation like subtraction also