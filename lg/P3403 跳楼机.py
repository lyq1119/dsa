import heapq
h = int(input())
h -= 1
a,b,c = map(int,input().split())
coins = sorted([a,b,c])
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
g = gcd(a,b)
g = gcd(g,c)
scaled_coins = [v // g for v in coins]
smallest = scaled_coins[0]
INF = float("inf")
dist = [INF] * smallest
dist[0] = 0
heap = [(0, 0)]
edges = [v for v in scaled_coins if v != smallest]
while heap:
    d, r = heapq.heappop(heap)
    if d != dist[r]:
        continue
    for w in edges:
        nr = (r + w) % smallest
        nd = d + w
        if nd < dist[nr]:
            dist[nr] = nd
            heapq.heappush(heap, (nd, nr))
h = h//g
total = 0
a = scaled_coins[0]
for i in range(a):
    if dist[i] != float("inf") and dist[i] <= h:
        total += (h-dist[i])//a + 1
print(total)