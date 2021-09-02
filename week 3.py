def add(a,b):
 return a+b
def sub(c,d):
 return c-d
def mul(e,f):
 return e*f
def div(g,h):
 return g/h
print("*******************")
print("1. TO PERFORM ADDITITON")
print("2. TO PERFORM SUBTRACTION")
print("3. TO PERFORM MULTIPICATION")
print("4. TO PERFORM DIVISION")
print("*******************")
choice = int(input("Enter Your choice:"))
if choice ==1:
    a=int(input("Enter the 1st value"))
    b=int(input("Enter the 2nd value"))
    print(add(a,b))
elif choice ==2:
    c=int(input("Enter the 1st value"))
    d=int(input("Enter the 2nd value"))
    print(sub(c,d))
elif choice ==3:
    e=int(input("Enter the 1st value"))
    f=int(input("Enter the 2nd value"))
    print(mul(e,f))
elif choice ==4:
    g=int(input("Enter the 1st value"))
    h=int(input("Enter the 2nd value"))
    print(div(g,h))
else:
 print("Please choose from the menu!!")


string=input(("Enter the string:"))  
if(string==string[::-1]):  
      print("The entered string is palindrome")  
else:
      print("The entered string is not palindrome")

      
def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    return fact

number=int(input(" Please enter any Number to find factorial :"))

factof= factorial(number)
print("The factorial of %d  = %d" %(number, factof))



list1=eval(input("enter a list1 : "))
list2=eval(input("enter a list2 : "))
if(len(list1))==len(list2):
    if (sorted(list1)==sorted(list2)):
      print("true")
      print(id(list1),id(list2))
    else:
      print("false")
else:
     print("false")
