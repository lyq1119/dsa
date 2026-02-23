mylist = input().split()
outputlist = []
stack = []
for s in mylist:
    if s.isdigit():
        outputlist.append(s)
    else:
        if not stack:
            stack.append(s)
        else:
            while stack:
                outputlist.append(stack.pop())
            stack.append(s)
while stack:
    outputlist.append(stack.pop())
print(*outputlist)