import sys


def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    weights = [0] + [int(next(it)) for _ in range(n)]
    values = [0] + [int(next(it)) for _ in range(n)]
    deps = [0] + [int(next(it)) for _ in range(n)]

    graph = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        if deps[i] != 0:
            graph[deps[i]].append(i)

    dfn = [0] * (n + 1)
    low = [0] * (n + 1)
    in_stack = [False] * (n + 1)
    stack = []
    comp_id = [0] * (n + 1)
    comp_count = 0
    timer = 0

    sys.setrecursionlimit(1000000)

    def tarjan(u):
        nonlocal timer, comp_count
        timer += 1
        dfn[u] = low[u] = timer
        stack.append(u)
        in_stack[u] = True

        for v in graph[u]:
            if dfn[v] == 0:
                tarjan(v)
                low[u] = min(low[u], low[v])
            elif in_stack[v]:
                low[u] = min(low[u], dfn[v])

        if low[u] == dfn[u]:
            comp_count += 1
            while True:
                x = stack.pop()
                in_stack[x] = False
                comp_id[x] = comp_count
                if x == u:
                    break

    for i in range(1, n + 1):
        if dfn[i] == 0:
            tarjan(i)

    comp_w = [0] * (comp_count + 1)
    comp_v = [0] * (comp_count + 1)
    indeg = [0] * (comp_count + 1)
    tree = [[] for _ in range(comp_count + 1)]

    for i in range(1, n + 1):
        cid = comp_id[i]
        comp_w[cid] += weights[i]
        comp_v[cid] += values[i]

    seen_edges = set()
    for i in range(1, n + 1):
        if deps[i] == 0:
            continue
        parent = comp_id[deps[i]]
        child = comp_id[i]
        if parent != child and (parent, child) not in seen_edges:
            seen_edges.add((parent, child))
            tree[parent].append(child)
            indeg[child] += 1

    root = 0
    tree.append([])
    comp_w.append(0)
    comp_v.append(0)
    for cid in range(1, comp_count + 1):
        if indeg[cid] == 0:
            tree[root].append(cid)

    neg_inf = -10**18

    def dfs(u):
        # dp[c]表示已经选了节点 u（对应 SCC），总容量为 c 时，从 u 的整棵子树能获得的最大价值。
        dp = [neg_inf] * (m + 1) 
        for cap in range(comp_w[u], m + 1):
            dp[cap] = comp_v[u]

        for v in tree[u]:
            child = dfs(v)
            merged = dp[:]
            for cap in range(m + 1):
                if dp[cap] == neg_inf:
                    continue
                rest = m - cap
                for extra in range(rest + 1):
                    if child[extra] != neg_inf:
                        total_cap = cap + extra
                        merged[total_cap] = max(
                            merged[total_cap],
                            dp[cap] + child[extra],
                        )
            dp = merged

        return dp

    print(dfs(root)[m])


if __name__ == "__main__":
    main()
