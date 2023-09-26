n=int(input('enter the number'))
rev=0
i=n
while(n>0):
    rev=(rev*10)+(n%10)
    n=n//10
print('reverse=',rev)    
if (i==rev):
    print('palindrom')
else:
   print('not palindrom')     