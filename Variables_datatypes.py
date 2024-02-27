#python automatically finds the type
name="Bharath"
age=23
price = 25.99
a= None
print(name)
print(type(age))
print(type(name))
print("My name:", name)
print("My age:",age)
print(a)
print(type(a))//NoneType

#rules for identifiers
# 1)identifiers can be combination of uppercase and lower case letters, digigts or an underscore(_).
# so myVariable, variable_1, variable_for_print all are valid python identifiers.
# 2)An identifier can not start with digit. So while variable1 is valie, 1variable is not value.
# 3) we can't use special symbols like !,#,@,%,$ etc in our identifier
# 4) identifier can be of any length

# Data types:
# integers(5,-25)
# string("bharath" or 'hello' or '''bharath''')
# float(24.4)
# Boolean(True or False)
# None(represent no value in it )

# Keywords:(reserved words)

# False      class      finally    is         return
# None       continue   for        lambda     try
# True       def        from       nonlocal   while
# and        del        global     not        with
# as         elif       if         or         yield
# assert     else       import     pass
# break      except     in         raise


#print the sum
a=1000
b=25
sum=a+b
print(sum)

# Types of Tokens
# Punctuators
# Punctuators are symbols to organize sentence structure in programming

# (),{},@,[],#

# -=,+=,/=,*=,//=,= etc.

# Python is implicit language because we don't define the types of data
# Java is explicit language because we  define the types of data

# Expression Exection
# -> String & Numeric values can operate together with *

A,B=2,3
Txt = "@"
print(2*Txt*3) # @@@@@@

# --> String & string can operate with +

C,D="2",3
Txt1 = "@"
print((C+Txt1)*D) #2@2@2@

#Numeric values can operate with all arithmetic operators
E,F = 2,3
G=4
print(E+F*G) #14

#Arithmetic expression with integer and float will result in float

H,I = 10,5.0
J=H*I
print(J)#50.0

#Result of division operator with two integers will be float

y,z = 1,2
x = y/z
k=y//z
print(x) #0.5
#print(k) # 0
# / gives float and // gives a int value

#Integer division with float and int will give int displayed as float

L,M = 1.5,3
O = L//M
print(O,L/M) #0.0 0.5 - 0.0 is a int only not float

# floor gives closest integer, which is lesser than or equal to the float value
# Result of(A//b) is same as floor (A/B)

# A,B=12,5
# c=A//B
# print(c) Ans :2

# A,B=-12,5
# c=A//B
# print(c) Ans - (-3) where ans will be is -2.4 but closest is -3 so the answer is -3 same for next oepration also
# for 2.5 the nearest will take 2 as ans in // division
# A,B=12,-5
# c=A//B
# print(c) Ans - (-3)