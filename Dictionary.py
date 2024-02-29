"""Dictionary in python
Dictionaries are used to store data values in key:value pairs

They are unordered, Mutable(changeable) & don't allow duplicate keys"""
#we can add lists and tuples in dictionary
dict={
    "name" : "Bharath",
    "cgpa" : 9.6,
    "marks" : [98,97,95],
    # we can make our key as int or float or anything also
    22 : 0,
}
print(dict["name"])
print(dict["marks"])
dict["cgpa"]=9.5
dict["age"]=23 #age will be included in dict
print(dict)

#dictionaries don't contain any indexes
#we can create empty dictionary
null_dict = {}
print(null_dict)

null_dict["name"] = "king"
print(null_dict)


#Nested Dictionaries

student = {
    "name":"Bharath",
    "score":{
        "chem":98,
        "phy":91,
        "math":90,
    }
}
print(student) #{'name': 'Bharath', 'score': {'chem': 98, 'phy': 91, 'math': 90}}
print(student["score"]) #{'chem': 98, 'phy': 91, 'math': 90}
print(student["score"]["phy"]) #91

#Dictionary Methods
# myDict.key() #returns all keys
# myDict.values() #returns all values
# myDict.items() #returns all (key,val) paris as tuples
# myDict.get("key") #returns the key according to value
# myDict.update(newDict) # inserts the specified items to the dictionaires


#to type cast print(list(student.key()))
#finding the length of the dict
print(len(student))
print(len(list(student.keys()))) #gives the length of the keys
print(list(student.values())) #['Bharath', {'chem': 98, 'phy': 91, 'math': 90}]
print(student.get("name")) #return the value of the key

#example case
#suppose
# print(student["name2"])# it will throw error
print(student.get("name2")) #it will give the output as no error-->none
student.update({"city":"Delhi"}) 
print(student) #{'name': 'Bharath', 'score': {'chem': 98, 'phy': 91, 'math': 90}, 'city': 'Delhi'}

new_di = {"sex":"male"}
student.update(new_di)
print(student) #new dict updated to old

