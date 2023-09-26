from random import *
a="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"
b=""
c=randint(65,92)
c=chr(c)
b=b+c
d=randint(97,124)
d=chr(d)
b=b+d
f=randint(35,39)
f=chr(f)
b=b+f
n=int(input("enter the range"))
for i in range(n-3):
  g=choice(a)
  b=b+g
print(b)

#import random
#a="abcdefghijklmnopqrstuvwxyz"
#b="123456789"
#c="#@$&*"
#pas = random.choice(a)+random.choice(b)+random.choice(a.upper())+random.choice(c)
#print(pas)
'''n=input("enter the password")
d=False
e=False
f=False
for i in n:
    if i.isupper():
        d=True
    elif i.islower():
        e=True
    elif i.isnumeric():
        f=True
if d and e and f:
    print("password set successfully")
elif d==False:
    print("add atleast one upper letter")
elif e==False:
    print("add atleast one lower letter")
elif f==False:
    print("add atleast one numeric")        '''

            



