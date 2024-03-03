from functools import reduce

nums=[1,2,3,4,5,6,7,8]
evens = list(filter(lambda n : n%2==0, nums))#returns even numbers
doubles = list(map(lambda n : n*2,evens)) #doubles the even number values
print(doubles)
sum = reduce(lambda a,b : a+b,doubles)
print(sum)