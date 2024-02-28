str1="This is a string."
str2 = 'Hello'
str2="""this is a string"""

#escape sequence character- to give special character to give formatting
#tab and next line we can do with the help of escape characters

str3 = "This is a string.\n And hii." #\n it is next line
print(str3)

str4 = "This is a apple.\t And banana" #\t tab
print(str4)

#operations in string

#concatination
# "hello"+"world"->"helloworld"
#length of str
print(len(str4))


#indexing - to access the elements in the strings
#strings are immutable
str5="Bharath"
print(str5[0]) #B
print(str5[5]) #t
print(str5[-1]) #h

#slicing
# Accessing parts of string
# str[starting_idx : ending_idx] # ending idx is not included
#from the starting element to before ending element it print
str6="heyprabhu"
print(str6[1:4]) #eyp #where four element is not included 
print(str6[3:len(str6)]) #yprabhu #index starts from zero
#same output
print(str6[3:]) #where it will go from 3 to end of the string
print(str6[:4]) #where it will go from zero to 4

#negative index
str7 = "apple"
# backward counting will start from -1
print(str7[-3:-1]) #pl where the ending index won't be included which is -1


#String Functions
str = "I am Coder."
str.endswith("er.") #returns true if string ends with substr
str.capitalize() #capitalizes 1st char

str.replace(old,next) #ex: str.replace("o","a") # it will replaces where ever o is their with a in the string #replaces all occurrences of old with new
str.find(word) #prints the character index and if it is a word return the first character index of the word #returns 1st index of 1st occurrence and if character not found returns -1

str.count("am") #counts the occurrence of substr in string #ans-1