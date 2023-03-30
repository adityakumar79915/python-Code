x,y=map(int,(input().split()))
if x==0 or y==0:
    print("origin")
elif x>0 or y>0:
    print("1st quad")
elif x<0 or y>0:
    print("2nd quad")
elif x<0 or y<0:
    print("3rd quad")
elif x>0 or y<0:
    print("4th quad")                