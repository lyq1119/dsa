s = input()
mylist = [ord(s[i])-64 for i in range(len(s))]
total = 0
for i in range(len(mylist)):
    total += (26**i) * mylist[-i-1]
print(total)