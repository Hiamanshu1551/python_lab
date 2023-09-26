a=input('enter the string')
b=input('enter the character')
c=0
for i in range(1,len(a)):
    if a[i]==b:
        c=c+1
    
print("frequency of a character",c)
