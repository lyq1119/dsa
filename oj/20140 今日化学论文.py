mystr = input()
n = len(mystr)
stack = []
cur = ""
flag = False
num = 0
for i in range(n):
    s = mystr[i]
    if s == "[":
        if flag:
            stack.append((num,cur))
            flag = False
            cur = ""
        if not mystr[i+1].isdigit():
            stack.append((1,cur))
        else:
            num = 0
            flag = True
    elif s.isalpha():
        if flag:
            stack.append((num,cur))
            flag = False
            cur = ""
        cur += s
    elif s.isdigit():
        num = 10*num + int(s)
    else:
        if flag:
            stack.append((num,cur))
            flag = False
            cur = ""            
        num1, curstr = stack.pop()
        cur = curstr + cur*num1
print(cur)
    