a=input("enter the string")
l=[]
l.extend(a)
print(l)
b=[]

for i in l:
    if i not in b:
        b.append(i)
print(b)        
