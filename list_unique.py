'''l=[]
l1=[]
n=int(input("enter the range "))
for i in range(n):
    l.append(int(input()))
print(l)
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)        '''


l=[]
l1=[]
n=int(input("enter the range "))
for i in range(n):
    l.append(int(input()))
print(l)
for i in l:
    if i%2==0:
        l1.append(i)

print(l1)
