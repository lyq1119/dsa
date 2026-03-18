from functools import lru_cache
@lru_cache(maxsize=None)
def length(num):
    if num <= 9:
        return num*(num+1)//2
    if num <= 99:
        return 45+(1+num)*(num-9)
    if num <= 999:
        return 9045+(3*num+84)*(num-99)//2
    if num <= 9999:
        return 1395495+(num-999)*(4*num+1786)//2
    if num <= 99999:
        return 189414495+(num-9999)*(5*num+27788)//2
def fun(num):
    left,right = 1,99999
    while left < right:
        if right-left == 1:
            if length(right) > num:
                return left
            return right
        mid = (left+right)//2
        if length(mid) > num:
            right = mid-1
        else:
            left = mid
    return left
for _ in range(int(input())):
    i = int(input())
    t = fun(i)
    s = i - length(t)
    if s == 0:
        print(int(str(t)[-1]))
    else:
        if s <= 9:
            print(s)
        elif s <= 189:
            m = (s+9)%2
            if m == 0:
                print(((s+9)//2)%10)
            else:
                print(int(str(((s+9)//2)+1)[m-1]))
        elif s <= 2889:
            m = (s+9*2+90)%3
            if m == 0:
                print(((s+9*2+90)//3)%10)
            else:
                print(int(str(((s+9*2+90)//3)+1)[m-1]))
        elif s <= 2889+9000*4:
            m = (s+9*3+90*2+900)%4
            if m == 0:
                print(((s+9*3+90*2+900)//4)%10)
            else:
                print(int(str(((s+9*3+90*2+900)//4)+1)[m-1]))
        elif s <= 2889+9000*4+90000*5:
            m = (s+9*4+90*3+900*2+9000)%5
            if m == 0:
                print(((s+9*4+90*3+900*2+9000)//5)%10)
            else:
                print(int(str(((s+9*4+90*3+900*2+9000)//5)+1)[m-1]))