#Loops
"""loops are used to repeat instructions.
while loops
while condition:
    #some work"""

# Break & continue
# Break: used to terminate the loop when encountered.
# continue: terminates execution in the current iteration & continue execution of the loop with the next iteration

cnt = 1;
while cnt<=5:
    print("Hello")
    cnt+=1

list = [1,2,3,4,5,6,7,8,100]
idx = 0
while idx<len(list):
    print(list[idx])
    idx+=1

tuple = (1,2,3,4,5,6,7,8,100)
idx = 0
search = 4
while idx<len(tuple):
    if(search==idx):
        print("found at",idx-1)
        break;
    idx+=1

i=0
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i) # 0 1 2 4 5
    i+=1

#if it meets the contion then i will be 3 then i+=1 then it will skip the printing and incrementing

"""#for loops in python
Loops are used fo rsequential traversal. For traversing list,string,tuples etc.
for loops
for el in list:
    #some work

for Loop with else:
    
for el in list:
    #some work
else:
    #work when loop ends """

nums = [1,22,44,5]
for val in nums:
    print("nums are:",val) 

tup = (7,8,9,5)
for num in tup:
    print(num)

str = "Bharath"
for char in str:
    print(char)
    #optional thing is else but else wont work in break cases
else:
    print("end")

#practice
#using for
#print the elements of the following list using a loop:
#[1,4,9,16,25,36,49,64,81,100]
li = [1,4,9,16,25,36,49,64,81,100]
for l in li:
    print(l)
#question2: search for a number x in this tuple using loop:
#[1,4,9,16,25,36,49,64,81,100]

t = (1,4,9,16,25,36,49,64,81,100)
x = 64
index = 0;
for i in t:
    if(i==x):
        print("Element found at index:",index)
        break
    index = index+1;

#range()
"""Range functions returns a sequence of numbers, starting from 0 by default, and increments by 1(by default), and stops before a specified number.

range(start?,stop,step?) step means how much you want to increase the gap  by default 1"""
for i in range(10): #range(stop)
    print(i) # 0 to 9

for i in range(2,10): #range(start,stop)
    print(i) # 2 to 9
for i in range(2,10,2): #range(start,stop,step)
    print(i) # 2,4,6,8

#even numbers
for i in range(2,100,2): #range(start,stop,step)
    print(i) # all even number 2 to 100
#odd number
for i in range(1,100,2): #range(start,stop,step)
    print(i) # all even number 1 to 100 odd numbers
#printing 100 to 1
for i in range(100,0,-1):
    print(i)
#multiplication table of n where n is 5
n = int(input("enter the number"))
for i in range(1,11):
    print(n*i)

#pass statement
#pass is a null statement that does nothing. it is used as a placeholder for future code.
# for el in range(10):
#     pass
#if we dont do any work in the loop we need to pass or else it will thorw the error expected an indented block
for i in range(5):
    #empty
    pass
print("some useful work")

