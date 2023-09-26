'''a=input("enter the string")
a=a.lower()
for i in range(97,123):
    if chr(i) not in a:
     print("not pangram")
     break
else:
   print("pangram")     '''


a=input("enter the string")
b="abcdefghijklmnopqrstuvwxyz"
for i in a:
    if i not in b:
        print("not pangram")
        break
else:
    print("pangram")    