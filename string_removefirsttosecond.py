a=input("enter the first string")

b=input("enter the second string")


c=''
for i in a:
    if i not in b:
        c=c+i
print(c)  

 