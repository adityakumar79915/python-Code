n=input()
for i in n:
    if i>='a' and i<='z':
        print(chr(ord(i)-32),end="")
    else:
        print(chr(ord(i)+32),end="")    