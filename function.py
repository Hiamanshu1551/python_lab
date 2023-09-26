def vote(age):
    if age>=18:
        return "eligible"
    else:
     return "not eligible"
a=int(input("enter the age"))
b=vote(a)
print(b)
    

