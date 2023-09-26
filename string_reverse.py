word = input("Input a word to reverse: ")
for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")

'''string = input()
s = string.split()[::-1]
l = []
for i in s:
     l.append(i)
print(" ".join(l))'''