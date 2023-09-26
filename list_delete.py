a=[]
size=int(input("enter the size"))
for i in range(size):
    val=int(input("enter the value"))
    a.append(val)
print("original list",a)
kay=int(input("enter the value to delete"))    
flag=0
for i in range(size):
    if a[i]==key:
        pos=i
        flag=1
        break
if flag==0:
    print("element not found")
else:
    for i in range(pos,size-1)
    a[i]=a[i+1]
a.pop()
print("new list",a)    
