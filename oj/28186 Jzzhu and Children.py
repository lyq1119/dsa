from collections import deque
queue = deque()
n,m = map(int,input().split())
mylist = list(map(int,input().split()))
for i in range(n):
    queue.append((i,mylist[i]))
while queue:
    if len(queue) == 1:
        print(queue[0][0]+1)
        break
    if queue[0][1] <= m:
        queue.popleft()
    else:
        i,num = queue.popleft()
        queue.append((i,num-m))