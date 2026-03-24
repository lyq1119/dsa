import sys
from collections import deque
data = iter(sys.stdin.read().split())
N = int(next(data))
D = int(next(data))
yudi = []
for _ in range(N):
    x = int(next(data))
    y = int(next(data))
    yudi.append((x,y))
yudi.sort()
upper = deque([yudi[0][1]])
lower = deque([yudi[0][1]])
b,e,d= 0,0,0
length = float("inf")
flag = True
while flag:
    flag = False
    while d < D:
        if e == N-1:
            break
        flag = True
        e += 1
        while upper and upper[-1] < yudi[e][1]:
            upper.pop()
        upper.append(yudi[e][1])
        while lower and lower[-1] > yudi[e][1]:
            lower.pop()
        lower.append(yudi[e][1])
        d = upper[0]-lower[0]
    if d >= D:
        length = min(length,yudi[e][0]-yudi[b][0])
    while d >= D and b < e:
        flag = True
        b += 1
        if upper and upper[0] == yudi[b-1][1]:
            upper.popleft()
        if lower and lower[0] == yudi[b-1][1]:
            lower.popleft()
        d = upper[0]-lower[0]
        if d < D:
            break
        else:
            length = min(length,yudi[e][0]-yudi[b][0])
if length != float("inf"):
    print(length)
else:
    print(-1)
        