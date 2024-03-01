#write a recursive function to calculate the sum of first n natural numbers.
def sum_n(n):
    if n==0:
        return 0
    return n+sum_n(n-1)
print(sum_n(5))
#write a recursive function to print all elements in a list.
#Hint: use list & index as parameters

def list_p(list,idx):
    if idx==len(list):
        return
    print(list[idx])
    list_p(list,idx+1)
list = [1,2,3,4,5]
list_p(list,0)
