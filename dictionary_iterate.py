d={}
n=int(input("enter the limit"))
for i in range(n):
    k=input()
    v=input()
    d[k]=v
  
print(d)
for i,j in d.items():
    print(i,j)
