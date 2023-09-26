def lucky_name(n):
    a="aeiou"
    f=True
    l=0
    for i in n:
        if i not in a:
            l+=1
    ans = len(n)-l
    if ans==5:
        print("lucky")
    else:
        print("not")

lucky_name(input("enter the name"))    
# d={}
# n=int(input())
# for i in range(n):
#     k=input()
#     v=input()
#     d[k]=v  
#     if lucky_name(v):
#         print("Roll No",k,"is Allowed")
#     else:
#         print("Roll No",k,"is not Allowed")


    
       