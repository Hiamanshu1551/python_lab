
lst=[]
a=int(input('enter the length'))
for i in range(1,a+1):
    l=int(input("enter the elment"))
    lst.append(l)
print(lst)
lst1=[]
lst2=[]
for i in lst:
    if i%2==0:
        lst1.append(i)
    else:
        lst2.append(i)   
print(lst2)   
print(lst1)