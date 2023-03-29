#check wheather a number is palindrome or not
'''n=int(input("enter number:"))
x=n
r=0
while(n>0):
    y=n%10
    r=r*10+y
    n=n//10
if(x==r):
    print("is palindrome")
else:
    print("not palindrome")'''
#using slicing
n=int(input("enter no:"))
x=int(str(n)[::-1])
if x==n:
    print("is palindrome")
else:
    print("not palindrome")
#PATTERNS
'''x=int(input("enter no:"))
for i in range(-1,x):
    print(" "*(1+i),end=" ")
    print("* "*(x-1-i))'''  
#question no 2
'''x=int(input("enter no:"))
for i in range(-1,x):
    print(" "*(x-i),end=" ")
    print("* "*(x-1-i))'''
#question no 3
'''x=int(input("enter no:"))
for i in range(-1,x):
    print(" "*(x-i),end="")
    print("* "*(i))
for j in range(-1,x):
    print(" "*(1+j),end="")
    print("* "*(x-1-j))'''
#question no 4
'''n=int(input("enter no:"))
print("pattern is:")
for i in range(1,n+1):
    for j in range(1,n+1):
     if(i==0 or i==n-1 or j==0 or j==n-1):
        print("*",end="")
else:
   print(" ",end="")'''
#question no 5
'''n=int(input("enter no:"))
for i in range(1,n+1):
    print("*"*i)'''
#question no 6
'''n=int(input("enter no:"))
for i in range(1,n+1):
    print(" "*(n-1),end="")
    print("*"*i)'''
 #question no 7
'''n=int(input("enter no:"))
for i in range(1,n+1):
    print(" "*(i-1))
    print("*"*(n+1-i))'''
#question no 8
x=(input("enter string"))
y=x.split()
print(len(y))
 
 



        

      
            
            
                   

    

         


