

n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
print(*l)    
    
for i in l:
    if i%2==0:
        ind = l.index(i)
        l[ind] = 0
        
    else:
        ind = l.index(i)
        l[ind] = 1
print(*l)   