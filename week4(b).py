#to filter only the even numbers from the given list
list_1=[]
n=int(input("Enter the size:"))
for i in range(0,n):
    ele=int(input())
    list_1.append(ele)
newList=list(filter(lambda x:x%2==0,list_1))
print(newList)