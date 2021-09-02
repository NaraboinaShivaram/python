#to find sum of numbers for the elements of the listby using reduce()

import functools
list_1=[]
n=int(input("Enter the size:"))
for i in range(0,n):
    ele=int(input())
    list_1.append(ele)
print(functools.reduce(lambda x,y:x+y,list_1))
