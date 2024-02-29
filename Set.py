#set in python
"""Set is the collection of the unordered items>
set is muttable but the elements are immutable
Each element in the must be unique & immutable

nums={1,2,3,4}
set2={1,2,2,2}

if we store any data type in set it will remain same it won't change
#repeated elements stored only one, so it resolved to {1,2}
null_set = set() #empty set syntax
# we can't store list and dict  in set.But we can add tuple"""

collection = {1,2,3,4,4,"hello"}
print(collection) #{1, 2, 3, 4, 'hello'}
print(type(collection)) #<class 'set'>
print(len(collection)) #5

# collection1 = {} #this would be the dict not set
# collection1 = set() #this would be the set for empty set

#Methods in set

# set.add(el) #adds an element
# set.remove(el) #removes the elem 
# set.clear() # empties the set
# set.pop() #removes a random value

collection1 = set()
collection1.add(1)
collection1.add(2)
collection1.add(3)
collection1.add(3)
collection1.add("hello")
collection1.add((5,6,7))
# collection.remove(2)
print(collection1)

#unhashable:which ever the values are immutable we can add in set beacuase it can form hash values
#collection1.clear()  it will return the output 0
#collection.pop() it will any random value

#Methods
#set.union(set2) # combines both set values & return new
#set.intersection(set2) # combines common values & returns new
set1 = {1,2,3}
set2 = {4,5,6}
print(set1.union(set2)) #op: {1, 2, 3, 4, 5, 6} #where set1 and set2 wont change it will remain same
set2.add(3)
print(set1.intersection(set2)) #{3}

