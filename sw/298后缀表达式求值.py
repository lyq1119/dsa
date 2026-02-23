outputlist = input().split()
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
