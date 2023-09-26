a=input("enter the first string")
l=[]
l.extend(a)
b=input("enter the second string")
l1=[]
l1.extend(b)

c=[]
for i in a:
    if i in b:
        c.append(i)
print(c)  