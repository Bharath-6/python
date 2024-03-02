#Methods 
# Methods are function that belong to objects.
#creatig class
class Student:
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks
    def hello(self):
        print("hello",self.name)
    def mark(self):
        print("Marks",self.marks)

#creating object
s1 = Student("karan",34)
s1.hello()
s1.mark()
s2 = Student("Bharath",55)
s2.hello()
s1.mark()

#Question: Create student class that takes name & marks of 3 subjects as arguments in constructor.Then create a method to print the average.
class Stu:
    def __init__(self,na,s1,s2,s3):
        self.na = na
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
    def average(self):
        sum = (self.s1+self.s2+self.s3)//3
        print("Average Marks of",self.na,"is:",sum)
m1 = Stu("Bharath",96,66,85)
m1.average()

    
#Anothe method
"""class Stu:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def average(self):
        sum = 0
        for val in self.marks:
            sum+=val
        print("hi",self.name,"Your average score is:",sum/3)
m1 = Stu("Bharath",[96,66,85])
m1.average() """