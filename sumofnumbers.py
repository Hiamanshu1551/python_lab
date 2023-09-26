n=int(input('enter the number'))
s=0
while (n>0):
    s=s+(n%10)
    n=n//10
print('sum of digits=',s)    

# product of digits
'''n=int(input())
while (n>0):
    p=p*(n%10)
    n=n//10
 print('product',p)'''   