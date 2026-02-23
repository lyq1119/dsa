def check(mylist):
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
    return flag
from itertools import permutations
n =  int(input())
for mylist in permutations([i for i in range(1,n+1)]):
    if check(mylist):
        print(*mylist)