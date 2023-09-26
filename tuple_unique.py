t=()
t1=()
n=int(input("enter the range "))
for i in range(n):
    e=input()
    t=t+(e,)
print(t)
for i in t:
    if i not in t1:
        t1=t1+(i,)
    else:
        print("repeated element is ",i)    
print("unique tuple",t1)        