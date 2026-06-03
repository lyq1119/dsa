from collections import defaultdict
n,m = map(int,input().split())
graph = defaultdict(list)
def has_cycle_dfs(graph,n):
    visited = [False] * n
    rec_stack = set()
    def dfs(i):
        visited[i] = True
        rec_stack.add(i)
        for neighbor in graph[i]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        rec_stack.remove(i)
        return False
    for i in range(n):
        if not visited[i]:
            if dfs(i):
                return True
    return False
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
if not has_cycle_dfs(graph,n):
    print("Yes")
else:
    print("No")