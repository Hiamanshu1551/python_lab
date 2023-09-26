'''a=input("enter the first string")

b=input("enter the secong string")
if sorted(a) ==sorted(b):
    print("anagram")
else:
    print("not anagram")    '''


a=input("enter the string")
l=sorted(a)                 #accending
l1=sorted(a,reverse=True)   #decending
print(l)
print(l1)