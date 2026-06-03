import heapq
def compare(sq1,sq2,n):
    heap = []
    res = []
    visited = [[False for _ in range(n)] for __ in range(n)]
    heapq.heappush(heap,(sq1[0]+sq2[0],0,0))
    visited[0][0] = True
    for _ in range(n):
        a,i,j = heapq.heappop(heap)
        res.append(a)
        if i < n-1 and not visited[i+1][j]:
            heapq.heappush(heap,(sq1[i+1]+sq2[j],i+1,j))
            visited[i+1][j] = True
        if j < n-1 and not visited[i][j+1]:
            heapq.heappush(heap,(sq1[i]+sq2[j+1],i,j+1))
            visited[i][j+1] = True
    return res
for _ in range(int(input())):
    m,n = map(int,input().split())
    sq1 = sorted(list(map(int,input().split())))
    if m == 1:
        print(*sq1)
        continue
    for _ in range(m-1):
        sq2 = sorted(list(map(int,input().split())))
        sq1 = compare(sq1,sq2,n)
    print(*sq1)