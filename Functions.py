#Functions in python
"""Block of statements that perform a specific task

def func_name(param1,param2..):
    #some work
    return val
func_name(arg1,arg2..) #function call 

where redudancy will decrease
There will be option no parameter ok it works or no return of anythign it will work
if a function wont return anything it will be none"""

def sum(a,b):
    s = a+b
    return s
a = 2
b=5
c=10
d=55
print(sum(a,b))
#if you want to use again and again
print(sum(c,d))
print(sum(5,4))

# Types of function 
"""1)user defined function
what ever we write is known as user defined function
2)Built-in functions
print()
len()
type()
range()"""

#if you want to print same thing in single
print("hey","all") #hey all we will get space between them
print("Bharath ", end="Mvs")
print(" From Gitam")


#Default parameters
# Assigning a default value to parameter, which is used when no argument is passed

def cal_prod(a1=1,b1=2):
    print(a1*b1)
    return a1*b1

cal_prod()

# def cal_prod(a1,b1=2):
#     print(a1*b1)
#     return a1*b1

# cal_prod(1) #where this case will work

#but if you do oppostie it like(a,b=2) and declar cal_prod(1) it will thorw error always first would be non default and second should be default
