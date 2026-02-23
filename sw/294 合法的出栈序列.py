n = int(input())
mylist = list(map(int,input().split()))
stack = []
cur = 1
flag = True
for num in mylist:
    if not stack:
        stack.append(cur)
    if stack[-1] > num:
        flag = False
        break
    elif stack[-1] == num:
        stack.pop()
    else:
        if cur > num:
            flag = False
        else:
            while cur <= num:
                stack.append(cur)
                cur += 1
            stack.pop()
if flag:
    print("Yes")
else:
    print("No")


    