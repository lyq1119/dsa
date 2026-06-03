from collections import deque
n,m,w = map(int,input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a,b,l = map(int,input().split())
    if l >= w:
        a -= 1
        b -= 1
        graph[a].append((b,l))
        graph[b].append((a,l))
def bfs(start):
    q = deque()
    q.append((start, 0)) 
    visited = {start}     # 必须用set，否则会mle 
    while q: # 强迫自己必须只能套一步while
        cur, step = q.popleft()
        if cur == n-1:
            return step
        for nxt,w in graph[cur]:
            if nxt not in visited:
                visited.add(nxt)
                q.append((nxt, step+1))
    return -1   # 找不到
print(bfs(0))