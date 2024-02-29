#Questions: store following word meanings in a python dictionary:
# table: "a piece of furniture", "list of facts & figures"
# cat:"a small animal"
dic = {
    "cat":"a small animal",
    "table":["a piece of furniture", "list of facts & figures"]
}
print(dic)

#Question: you are given a list of subjects for students.Assume one classroom is required for 1 subject.how many classrooms are needed by all students.

""" "python","java","C++","python","JavaScript",
"java","python","java","C++","C" """

#set
classroom={"python","java","C++","python","JavaScript",
"java","python","java","C++","C"}
print((classroom)) #op: {'python', 'C++', 'C', 'JavaScript', 'java'}
print(len(classroom))  #op: 5

#question: wap to enter marks of 3 subjects from the user and store them in dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value
marks = {

}
x = int(input("Enter marks of py"))
marks.update({"phy":x})
x = int(input("Enter marks of ch"))
marks.update({"ch":x})
x = int(input("Enter marks of maths"))
marks.update({"maths":x})
print(marks) #{'phy': 35, 'ch': 55, 'maths': 36}
#question: figure out a way to store 9 & 9.0 as separate values in the set.abs*you can take help of built-in data types
#set
values = {9,9.0}
print(values) # op: 9 # it will print 9 because python wil understand 9.0 and 9 as same 
#but if u take 9, 9.25 it will print 9 and 9.25
#possible 1 is 
#store 9 as int and "9.0" as a string
#possible 2 is 
"""values = {
 ("float",9.0),
 ("int",9)
 }
print(values) """