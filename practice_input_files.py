#create a new file "Practice.txt" using python.Add the following data in t:
"""Hi everyone
we are learning File I/O
using java
i Like programming in java"""
with open("Practice.txt","w") as f:
    f.write("Hi everyone \nwe are learning File I/O ")
    f.write("\nUsing java \ni Like programming in java")
#waf that replaces all occurrences of "Java" with "python" in above file.
with open("Practice.txt","r") as f:
    data = f.read()
new = data.replace("java","python")
print(new)
"""search if the word "learning " exists in the file or not """

word = "learning"
with open("Practice.txt","r") as f:
    data = f.read()
    if(data.find(word)!=-1):
        print("Found")
    else:
        print("Not Found")

"""anytime to use as a function
def check_for_word():
    word = "learning"
    with open("Practice.txt","r") as f:
    data = f.read()
    if(data.find(word)!=-1):
        print("Found")
    else:
        print("Not Found")
check_for_word()"""

#question: waf to find in which line of the file does the wor "learning" occur first.
#print-1 if word not found.abs
word = "learning"
with open("Practice.txt","r") as f:
    data = f.read()
    if(word in data):
        print("Found")
    else:
        print("Not Found")
def check_for_line():
    word = "learning"
    data = True
    line_no=1
    with open("Practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return 
            line_no+=1
    return -1
check_for_line()
#form a file containing numbers separated by comma, print the count of even numbers.
count=0
with open("nums.txt","r") as f:
    data = f.read()
    print(data)
    #find take indiviudals numbers and parse indiviudal elements/ type cast to integer values beacuse all in the form of string

    # num = ""
    # for i in range(len(data)):
    #     if(data[i]==","):
    #         print(int(num))
    #         num = ""
    #     else:
    #         num+=data[i]

    #another method
    num = data.split(",")
    for val in num:
        if(int(val)%2==0):
            count+=1
print(count) #total number of even numbers = 4



