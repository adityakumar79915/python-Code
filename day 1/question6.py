n=int(input())
ans = 0
while n!=0:
    y=n%10
    n=n//10
    ans=ans+y
print(ans)