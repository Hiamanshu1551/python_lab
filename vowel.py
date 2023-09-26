str = input("Enter a string: ")
vowel = "aeiou"
v=0
c=0
d=0
w=0
for i in str:
    if i in vowel:
        v+=1
    elif i == " ":
        w+=1
    elif i.isnumeric():
        d+=1
    elif i.isalpha():
        c+=1

print(f"Vowel: {v} Consonant: {c} Digit: {d} WhiteSpace: {w}")