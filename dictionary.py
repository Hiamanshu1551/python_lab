d={}
n=int(input("enter the limit"))
for i in range(n):
    k=input()
    v=input()
    d[k]=v
print("original dictionay")    
print(d)
d1={}
n1=int(input("enter the limit"))
for i in range(n1):
    k1=input()
    v1=input()
    d1[k1]=v1
d.update(d1)
print("new dictionary")
print(d)



