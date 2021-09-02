#use map function to double all the elements in the list 
list_1=[]
n=int(input("Enter the size:"))
for i in range(0,n):
    ele=int(input())
    list_1.append(ele)
newList=list(map(lambda x:x*2,list_1))
print(newList)