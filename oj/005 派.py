import math
n,f = map(int,input().split())
mylist = list(map(int,input().split()))
mylist = [x**2 for x in mylist]
left,right = 0,max(mylist)
def check(i):
    if i == 0:
        return False
    return sum([num//i for num in mylist]) >= 1+f
while right - left >= 10**(-6):
    mid = (left+right)/2
    if check(mid):
        left = mid
    else:
        right = mid
print(f"{right*math.pi:.3f}")