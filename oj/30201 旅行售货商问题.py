from collections import deque
n = int(input())
cost = []
for _ in range(n):
    cost.append(list(map(int,input().split())))
k = (1<<n)
matrix = [[float("inf") for _ in range(n)] for __ in range(k)]
matrix[1][0] = 0
minimum = float("inf")
for visit in range(2,k):
    for cur in range(1,n):
        if visit & 1 == 0:
            continue
        if (1<<cur)|visit != visit:
            continue
        visitnew = visit - (1<<cur)
        for i in range(n):
            if (1<<i)|visitnew != visitnew:
                continue
            a = matrix[visitnew][i]+cost[cur][i]
            if a >= matrix[visit][cur]:
                continue
            matrix[visit][cur] = a
for i in range(1,n):
    minimum = min(minimum,cost[i][0]+matrix[k-1][i])
print(minimum)