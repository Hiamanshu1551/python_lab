n=int(input('enter the number'))
t=n
s=0

while(n>0):
    s=s+(n%10)*(n%10)*(n%10)
    n=n//10
if(t==s):
    print('armstrong')   
else:
    print('not armstrong')      
