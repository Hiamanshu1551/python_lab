list=[]
a=input()
list.extend(a)
max = list[ 0 ]
for a in list:
        if a > max:
            max = a
print(max)        