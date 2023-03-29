n=str(input("enter values"))
cnt=0
for i in n:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        cnt=cnt+1
print("no of vowels")
print(cnt)