# if-elif-else(Syntax)

"""if(condtion):
    statement1
elif(condition):
    statement2
else:
    statementN """

light = input("light: ")
if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("look")
elif(light=="gree"):
    print("go")
else:
    print("Light is broken")

# and and or is used in python not || &&

#single line if / Ternary operator

# <var> = <val1> if <condition> else <val2>

food = input("food: ")
eat = "yes" if food=="cake" else "no"
print(eat)

#stt1> if <condition> else <stt2>

food = input("food : ")
print("sweet") if food=="cake" or food == "jalebi" else print("not sweet")

# clever if / Ternary operator
# <var> = (false_val,true_valu) [<condition>]
age = int(intput("age: "))
vote = ("yes", "no") [age>=18]

sal = float(input("salary : "))
tax=sal*(0.1,0.2) [sal<=50000]
print(tax)

