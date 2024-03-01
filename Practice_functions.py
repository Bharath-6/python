#waf to print the length of a list.(list is the parameter)
def len_list(list1):
    print(len(list1))
list1 = ["nn","hh","r","e"]
list2 = ["heors","hh","r","e","k"]
len_list(list1)
len_list(list2)
#waf to print the elements of a list in a single line.(list is the parameter)
def single_line(list):
    for i in list:
        print(i,end=" ")
single_line(list1)
#waf to find the factoiral of n.(n is the parameter)
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact
n = 5
print(factorial(n))
#waf to convert usd to INR.n
def convert_Inr(d):
    print("USD:",d,"The money dollar converted to rupees is:",d*82.87)
dollar = 7
convert_Inr(dollar)
