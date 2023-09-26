'''t=()
n=int(input("enter the limit"))
for i in range(n):
    e=input()
    t=t+(e,)
print(t)'''

tuple=5,10,15,20
print(tuple)       #packing
n1, n2, n3,n4=tuple
print(n1,n2,n3,n4)  #unpacking
tuple=5,
print(tuple)
#to add an items in tuple first make list then use  
# append method to add th items and then convert to tuple