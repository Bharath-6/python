#File I/O in python
 
"""python can be used to perform operations on a file.(read & write data)

Types of all files

1) Text Files: .text, .docx, .log etc.
2) Binary Files : .mp4,.mov,.png,.jpeg etc. """

"""we have to open a file before reading or writing.

f=open("file_name","mode")
file_name would be sample.txt or demo.docx

mode:
r:read mode
w:write mode

data = f.read()
f.close 

by default read mode"""
# if ur working on same folder u can just provide file name if you want to access the outside file then you need to mention whole location copy path of file
f = open("demo.txt","r")
data = f.read()
print(data) #I am learning python
# f.close()

#when u use f.read then it will read everything if try to print f.readline it gives empty space wont print a line beacuse already it is readed
line1 = f.readline()
print(line1) #I am learning python
line2 = f.readline()
print(line2) #How are you
#to read only first 5 character
"""f = open("demo.txt","r")
data = f.read(5)
print(data) #I am learning python
f.close()"""

# data = f.read() #reads entire file
# data = f.readline() #reads one line at a time and we will get extra space line after printing the first line


#writing to a file
f = open("demo.txt","w")
f.write("this is a new line") #overwrites the entire file

f=open("demo.txt","a")
f.write("\nthis is Bharath") #adds to the file
f.close()


#if file try to open unexisting file in w mode if it wont their then it automatically creates a new fild
f=open("sample.txt","a")
f.write("Hello this is Bharath") #adds to the file
f.close()


#r+ read+ overwrite (ptr start) - no truncate
#w+ "       "                   - truncate
#a+  "     append       (prt end) - no truncate

#with syntax
"""with open("demo.text","a") as f:
    data = f.read() #it's not complusory to close beacuse it automatically takes"""

#Deleting a fild
"""using the os module
Module(list a code library) is  a file written by another programmer that generally has a functions we can use.

import os 
os.remove(filename)
"""

#if any modules not able to import use pip install or pip3 install

""" "r" (Read):
Meaning: Opens the file for reading.
Use Case: Suitable for tasks where you only need to read the contents of the file.

"w" (Write):
Meaning: Opens the file for writing. If the file already exists, it truncates the file to zero length. If the file does not exist, it creates a new file.
Use Case: Useful for tasks where you need to write data to a file, and it's okay to overwrite existing content.

"a" (Append):
Meaning: Opens the file for writing, but if the file exists, it appends the new data to the end of the file.
Use Case: Appropriate when you want to add new data to an existing file without erasing the previous content.

"b" (Binary Mode):
Meaning: Opens the file in binary mode, indicating that the data being written or read is in binary format.
Use Case: Necessary when working with non-text files, such as images or executable files.

"x" (Exclusive Creation):
Meaning: Opens the file for exclusive creation. If the file already exists, the operation will fail.
Use Case: Ensures that a file with the same name doesn't already exist before creating a new one.

"+" (Read and Write):
Meaning: Opens the file for both reading and writing.
Use Case: Useful when you need to perform both read and write operations on the same file."""
