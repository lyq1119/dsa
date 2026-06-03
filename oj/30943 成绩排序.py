n,m = map(int,input().split())
graph = [[False]*n for _ in range(n)]
for _ in range(n):
    graph[_][_] = True
for _ in range(m):
    a,b,c = map(int,input().split())
    if c == 0:
        graph[a][b] = True
    else:
        graph[b][a] = True
def floyd_warshall(graph):
    # graph 是一个邻接矩阵，如果两点不连通，值为 float('inf')
    # graph[i][i] = 0
    # 节点数量
    n = len(graph)
    # 初始化距离矩阵 dist
    # 核心算法：三层循环
    # 注意：k（中间点）必须在最外层！
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # 如果通过中间点 k 的路径更短，则更新
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True
    count = 0
    for i in range(n):
        verdict = True
        for j in range(n):
            verdict = verdict and (graph[i][j] or graph[j][i])
        if verdict:
            count += 1
    return count
print(floyd_warshall(graph))