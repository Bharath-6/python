"""Lists in Python

A built-in data type that stores set of values

it can store elements of different types(integer, float,string,etc)

marks = [87,64,33,95,76] # marks[0] marks[1]..
student = ["kaaran",85,"Delhi"] #student[0],student[1]..
student[0] = "arjun" #allowed in python

len(student) #return length"""

# for using different variables for different data types it is so difficult to take rather we would be using list

marks = [33,44.5,22,11]
print(marks[0])
marks[1]= "hello"
print(marks[1])
print(len(marks))

#in java we use array to store the similar elements but in python we use list to store different data types

#strings - immutable 
# where we can access the element but we can't change it
#lists - muttable  
# - where you can access the element and you can change the element

# List Slicing

# similar to string slicing
# same slicing rules in a string in python for list
# list_name[starting_idx:ending_idx] # ending idx is not included
student=[87,64,33,95,76]
print(student[1:4]) #op:[64,33,95]
print(student[:4]) #is same as marks[0:4]
print(student[1:]) #is same as marks[1:len(marks)]
print(student[-3:-1]) #is [33,95]

# List Methods:
# list = [2,1,3]
# print(list.sort()) # it will print same elements
# print(list) # now it will print the sorted list

#list2 = [2,1,3]
#print(list2.append(4)) # it will print None it will append but wont return any answer. if you append first then print it will give the answer like:

#list2.append(4)
#print(list) then it wil append


list = [2,1,3]
list.append(4) #adds one element at the end [2,1,3,4]
print(list)
list.sort() #sorts in ascending order [1,2,3,4] #we cant do this list = list.sort() print(s)
print(list)
list.sort(reverse = True) #sorts in descending order [4,3,2,1]
print(list)
#now the list is 4,3,2,1 if perform reverse on it it wil be
list.reverse() #reverses list [1,2,3,4]
print(list)
# list.insert(idx,el) #insert element at index
# print(list)
list.insert(1,2)
print(list) #[1, 2, 2, 3, 4]

#remove
list.remove(2) #remove first occurence of element [[1, 2, 3, 4]]
print(list)
#pop
#removes the particular index
list.pop(0)
print(list) # [2, 3, 4]


#Tuples
# A build-in data type that lets us create immutable sequences of values.

# list - muttable
# string and tuple - immutable
tup = (2,1,3,4)
print(type(tup)) #op: <class 'tuple'>
print(tup[0]) #2
print(tup[1]) #1
# the below cannot be done in tuple
# tup[0] = 5 #op: error tuple object does not support item assignment
#we can create empty tuple
tupu = ()
#single value tuple
tup1 = (1,) #if we remove comma then python will understand as a integer  then it would int
# for multiple value  at end no need of keeping comma like (3,2,1)
print(tupu) #()
print(type(tupu)) #<class 'tuple'>

# slicing like a list in tuple as well
print(tup[1:3]) #(1, 3)

# Tuple Methods
# tup = (2,1,3,1)
# tup.index(el) #return index of first occurrence tup.index(1) is 1
# tup.count(el) #counts total occurrences tup.count(1) is 2

#practice
# questions: wap to check if a list contains a palindrome of elements.(hint: use copy() method)
#copy is a duplicate of list
#the process of checking list is palindrome or creates a copy of list and reverse it and check the copy and orginal or equal if it is equal then it is palidrome or else not palidrome
list1 = [1,2,1]
list2 = [1,2,3]
copy_list = list1.copy()
copy_list.reverse()
if(copy_list == list1):
    print("palidrome")
else:
    print("Not palidrome")
#ans : palidrome
#if you check fro list2 it is not a palidrome