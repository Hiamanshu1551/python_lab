'''12345
   1234 
   123
   12
   1'''
'''n=int(input())
for i in range(n,0,-1):
    print("")
    for j in range(1,i+1):
        print(j,end=" ")'''


'''1
   12
   123
   1234
   12345'''
n=int(input())
for i in range(1,n+1):
    
    for j in range(1,i+1):
        print(j,end=" ")
    print("")

'''    1
      12
     123 
    1234
   12345'''
  

n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(end=" ")
    for k in range(i+1):    
        print(i,end=" ")
    print()  