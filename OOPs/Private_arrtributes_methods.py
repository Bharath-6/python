#Private(like) attributes & Methods
""" Conceptual implementation in python
Private attributes & methods are meant to be used only within the class and are not accessible from outside the class"""
# keep double underscore before like example below acc pass
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
    def reset_pass(self):
        print(self.__acc_pass) #this is used to access the accpass which is in inside the class it will print
acc1 = Account("123456","abc")
print(acc1.__acc_pass) #AttributeError: 'Account' object has no attribute '__acc_pass'(now it is private we cannot access the out of the class)
#we can access from the inside class where we will create a function in the class. name is reset
print(acc1.reset_pass()) #abc

#we can make any function or method private using __