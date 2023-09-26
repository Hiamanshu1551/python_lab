t=()
n=int(input("enter the range "))
for i in range(n):
    e=input()
    t=t+(e,)
print(t)
c=input("enter element to fnd index")
a=t.index(c)
print(a)