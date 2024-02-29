#Loops
"""loops are used to repeat instructions.
while loops
while condition:
    #some work"""

# Break & continue
# Break: used to terminate the loop when encountered.
# continue: terminates execution in the current iteration & continue execution of the loop with the next iteration

cnt = 1;
while cnt<=5:
    print("Hello")
    cnt+=1

list = [1,2,3,4,5,6,7,8,100]
idx = 0
while idx<len(list):
    print(list[idx])
    idx+=1

tuple = (1,2,3,4,5,6,7,8,100)
idx = 0
search = 4
while idx<len(tuple):
    if(search==idx):
        print("found at",idx-1)
        break;
    idx+=1