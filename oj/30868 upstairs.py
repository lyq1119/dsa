import sys
import heapq
def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    a = int(next(it))
    b = int(next(it))
    c = int(next(it))
    q = int(next(it))
    if q == 0:
        return
    queries = [int(next(it)) for _ in range(q)]
    coins = []
    for v in (a, b, c):
        if v > 0:
            coins.append(v)
    coins = sorted(set(coins))
    if not coins:
        out = []
        for h in queries:
            out.append("Yes" if h == 0 else "No")
        print("\n".join(out_lines))
        return
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    g = coins[0]
    for v in coins[1:]:
        g = gcd(g, v)
    if len(coins) == 1:
        step = coins[0]
        out = []
        for h in queries:
            if h == 0 or (step > 0 and h % step == 0):
                out.append("Yes")
            else:
                out.append("No")
        print("\n".join(out_lines))
        return
    # Scale by gcd so the gcd becomes 1 for the residue calculations.
    scaled_coins = [v // g for v in coins]
    smallest = scaled_coins[0]
    # Dijkstra on residues modulo smallest coin.
    INF = 10**30
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
    out_lines = []
    for h in queries:
        if h == 0:
            out_lines.append("Yes")
            continue
        if h % g != 0:
            out_lines.append("No")
            continue
        h_scaled = h // g
        r = h_scaled % smallest
        if h_scaled >= dist[r]:
            out_lines.append("Yes")
        else:
            out_lines.append("No")
    print("\n".join(out_lines))
if __name__ == '__main__':
    main()
