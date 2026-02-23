import sys,heapq
data = iter(sys.stdin.read().split())
while True:
    try:
        n = int(next(data))
        matrix = [[int(next(data)) for _ in range(n)] for __ in range(n)]
        visited = {0}
        total = 0
        queue = []
        for i in range(1,n):
            heapq.heappush(queue,(matrix[0][i],0,i))
        while queue:
            fibre,i,j = heapq.heappop(queue)
            if j in visited:
                continue
            total += fibre
            visited.add(j)
            for t in range(n):
                if t not in visited:
                    heapq.heappush(queue,(matrix[j][t],j,t))
        print(total)
    except StopIteration:
        break