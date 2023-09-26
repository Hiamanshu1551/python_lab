d={}
n=int(input("enter the limit"))
for i in range(n):
    k=input()
    v=input()
    d[k]=v
print(d)  
print(sum(d.values()))


'''my_dict = {'data1':100,'data2':-54,'data3':247}
print(sum(my_dict.values()))'''