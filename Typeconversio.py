# Type Conversion

"""Conversion
python interpeter automatically convert

Casting
Manually we will convert"""

a,b = 1,2.54
sum=a+b
print(sum) #op: 3.54 #python will automatically convert int to float 

c,d = 1.2,"10"
print(c+d) #error unsupported operand type(s) for +: 'float' and 'str'

# we convert manually and string to int and we can perform the operation

A,B = 1,"2"
C=int(B)
sum=A+C
print(sum)
print(type(C)) #int
#we can't type cast string contain character to float 



