n=int(input("enter year:-"))
if n%100==0:
    if n%400==0:
        print("leap year")
    else:
        print("not leap year")
else:
    if n%4==0:
        print("leap year")
        




