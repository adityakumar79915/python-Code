n=int(input())
cnt=0
for i in range(1,n+1):
    if n%i==0:
        cnt=cnt+1
    if cnt==2:
        print("prime")
    else:
        print("not prime")        