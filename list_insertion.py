a=[]
size=int(input("enter the size"))
for i in range(size):
    val=int(input("enter value"))
    a.append(val)
print("original value",a)    
key=int(input("enter the value to insert"))
pos=int(input("enter the position to insert"))
a.append(None)
for i in range(size-1,pos-2,-1):
    a[i+1]=a[i]

a[pos-1]=key 
print("new list",a)   
    

