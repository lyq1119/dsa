p = int(input())
id = {}
locs = []
for i in range(p):
    loc = input()
    id[loc] = i
    locs.append(loc)
q = int(input())
linjiejuzhen = [[float("inf")]*p for _ in range(p)]
for _ in range(p):
    linjiejuzhen[_][_] = 0
for _ in range(q):
    loc1,loc2,dis = input().split()
    i1 = id[loc1]
    i2 = id[loc2]
    dis = int(dis)
    linjiejuzhen[i1][i2] = min(linjiejuzhen[i1][i2],dis)
    linjiejuzhen[i2][i1] = min(linjiejuzhen[i2][i1],dis)
n = len(linjiejuzhen)
# 初始化距离矩阵 dist
dist = linjiejuzhen
next_node = [[j for j in range(n)] for i in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            # 如果通过中间点 k 的路径更短，则更新
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                next_node[i][j] = next_node[i][k]
def solve(loc1,loc2):
    i1 = id[loc1]
    i2 = id[loc2]
    cur = i1
    path = [loc1]
    if i1 == i2:
        return path
    while next_node[cur][i2] != i2:
        path.append("("+str(dist[cur][next_node[cur][i2]])+")")
        path.append(locs[next_node[cur][i2]])
        cur = next_node[cur][i2]
    path.append("("+str(dist[cur][i2])+")")
    path.append(loc2)
    return path
r = int(input())
for _ in range(r):
    loc1,loc2 = input().split()
    path = solve(loc1,loc2)
    print("->".join(path))