d={}
n=int(input("enter the limit "))
for i in range(n):
    k=input()
    v=input()
    d[k]=v
print(d)    

t=sorted(d.items(), key=lambda k: k[1])
print(t)
t1=sorted(d.item(),key=lambda k:k[1],reverse=True)
print(t1)
