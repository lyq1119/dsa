from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)
def tarjan_scc(n, adj):
    dfn = [-1] * n      # 搜索次序
    low = [-1] * n      # 最低链接值
    stack = []          # 辅助栈
    in_stack = [False] * n
    timer = 0
    sccs = []           # 存储最终结果
    def dfs(u):
        nonlocal timer
        dfn[u] = low[u] = timer
        timer += 1
        stack.append(u)
        in_stack[u] = True
        for v in adj[u]:
            if dfn[v] == -1: # 情况 A：邻居未访问
                dfs(v)
                low[u] = min(low[u], low[v])
            elif in_stack[v]: # 情况 B：邻居在栈中（回边）
                low[u] = min(low[u], dfn[v])
        # 判定强连通分量的根
        if low[u] == dfn[u]:
            current_scc = []
            while True:
                node = stack.pop()
                in_stack[node] = False
                current_scc.append(node)
                if node == u:
                    break
            sccs.append(current_scc)
    for i in range(n):
        if dfn[i] == -1:
            dfs(i)        
    return sccs

n = int(input())
costs = list(map(int,input().split()))
m = int(input())
adj = defaultdict(list)
for _ in range(m):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    adj[a].append(b)

sccs = tarjan_scc(n,adj)
min_cost = 0
num_ways = 1
# 给每个点分配SCC编号
scc_id = [0] * n
for i in range(len(sccs)):
    min_i = float("inf")
    count_i = 0
    for node in sccs[i]:
        if costs[node] < min_i:
            min_i = costs[node]
            count_i = 0
        if costs[node] == min_i:
            count_i += 1
        scc_id[node] = i
    min_cost += min_i
    num_ways *= count_i
print(min_cost,num_ways%(10**9+7))