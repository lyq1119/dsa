mylist = input().split()
outputlist = []
stack = []
curnum = ""
flagshu = True
for s in mylist:
    if s.isdigit():
        flagshu = True
        curnum += s
    else:
        if flagshu:
            if curnum:
                outputlist.append(curnum)
                curnum = ""
            flagshu = False
        if not stack:
            stack.append(s)
        else:
            if s == "*" or s == "/":
                while stack and (stack[-1] == "*" or stack[-1] == "/"):
                    outputlist.append(stack.pop())
                stack.append(s)
            else:
                while stack:
                    outputlist.append(stack.pop())
                stack.append(s)
if curnum:
    outputlist.append(curnum)
while stack:
    outputlist.append(stack.pop())
print(*outputlist)