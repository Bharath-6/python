#Recursion 
#when a function calls itself repeadtedly is known as recursion

#prints n to 1 backwards
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

n = 5
show(n)

# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
#     print("End")

# n = 5
# show(n)
"""5
4
3
2
1
End
End
End
End
End"""

#factorial
#return n!
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(6))