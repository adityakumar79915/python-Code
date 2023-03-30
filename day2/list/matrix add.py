row=int(input("enter row"))
column=int(input("enter column"))
n1=[]
print("enter elements in matrix 1")
for i in range(row):
    l=[]
    for j in range(column):
        l.append(float(input()))
    n1.append(l)
print(f"matrix1=[n1]")  
n2=[]
print("enter elements in matrix 2")
for i in range(row):
    l=[]
    for j in range(column):
        l.append(float(input()))
    n2.append(l)
print(f"matrix2=[n2]")
result=[]
for i in range(row):
    l=[]
    for j in range(column):
        l.append(n1[i][j]+n2[i][j])
    result.append(l)    
for i in range(row):
    for j in range(column):
        print(f"{result[i][j]:10}",end="")
    print("")                             
         