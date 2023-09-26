a=[]
size=int(input("enter the size"))
for i in range(size):
    val=int(input("enter value"))
    a.append(val)
print("original value",a) 
key=a[0]
for i in range(1,size):
    a[i-1]=a[i]
a[size-1]=key

print("new list",a)    
