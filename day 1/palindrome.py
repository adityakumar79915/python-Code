n=int(input("enter number:"))
x=n
r=0
while(n>0):
    y=n%10
    r=r*10+y
    n=n//10
if(x==r):
    print("is palindrome")
else:
    print("not palindrome")