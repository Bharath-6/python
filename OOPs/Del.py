#del keyword
#used to delete object prperties or object itself.abs
""" del s1.name
del s1 """
class Student:
    def __init__ (self,name):
        self.name = name

s1 = Student("bharath")
print(s1.name) #bharath
del s1
print(s1.name) #NameError: name 's1' is not defined
