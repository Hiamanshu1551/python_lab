n=int(input())
l=[]
for i in range(n):
    l.append(input())
print(l)
res = max(l, key = len)
print("Maximum length string is : " + res)