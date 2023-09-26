l=[]
n=int(input("enter the range "))
for i in range(n):
    l.append(input())
print(l)
a=sorted(l,key=len)
print(a)

    
