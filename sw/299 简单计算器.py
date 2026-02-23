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
def qiuzhi(mylist):
    stack = []
    for s in mylist:
        if s != "*" and s != "+" and s != "-" and s != "/":
            stack.append(float(s))
        else:
            b = stack.pop()
            a = stack.pop()
            if s == "+":
                stack.append(a+b)
            elif s == "-":
                stack.append(a-b)
            elif s == "*":
                stack.append(a*b)
            elif s == "/":
                stack.append(a/b)
    return f"{stack[0]:.2f}"
print(qiuzhi(outputlist))