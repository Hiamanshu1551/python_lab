d=int(input('enter the date '))
m=int(input('enter the month'))
print(f'{d}/{m}/2019')
sum=0
for i in range(1,m+1):
    a=(i<=7)*(30+(i%2))+(i>7)*(31-(i%2))-28*(i==2)
    sum=sum+a
print(f'no. of days left in year is {365-(sum+d)}')