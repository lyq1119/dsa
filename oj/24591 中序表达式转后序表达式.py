import sys
input = sys.stdin.read()
data = input.split()
k = int(data[0])
i = 1
for _ in range(k):
    mystr = data[i]
    num = ""
    output = []
    flagshu = True
    stack = []
    for s in mystr:
        if s.isdigit():
            flagshu = True
            num += s
        elif s == ".":
            flagshu = True
            num += s
        elif s == "*" or s == "/":
            if flagshu:
                flagshu = False
                if num:
                    output.append(num)
                num = ''
            while stack:
                a = stack.pop()
                if a == "(" or a == "+" or a == "-":
                    stack.append(a)
                    stack.append(s)
                    break
                else:
                    output.append(a)
            if not stack:
                stack.append(s)
        elif s == "(":
            if flagshu:
                flagshu = False
                if num:
                    output.append(num)
                num = ''
            stack.append(s)
        elif s == ")":
            if flagshu:
                flagshu = False
                if num:
                    output.append(num)
                num = ''
            while True:
                a = stack.pop()
                if a == "(":
                    break
                output.append(a)
        elif s == "+" or s == "-":
            if flagshu:
                flagshu = False
                if num:
                    output.append(num)
                num = ''
            while stack:
                a = stack.pop()
                if a == "(":
                    stack.append(a)
                    stack.append(s)
                    break
                else:
                    output.append(a)
            if not stack:
                stack.append(s)            
    if num:
        output.append(num)
    while stack:
        output.append(stack.pop())
    print(*output)
    i += 1