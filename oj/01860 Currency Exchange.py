N,M,S,V = map(float,input().split())
N,M,S = int(N),int(M),int(S)
S -= 1
graph = [[None for _ in range(N)] for __ in range(N)]
for t in range(M):
    A,B,Rab,Cab,Rba,Cba = map(float,input().split())
    A -= 1
    B -= 1
    A,B = int(A),int(B)
    graph[A][B] = (Rab,Cab)
    graph[B][A] = (Rba,Cba)
cur = [-float("inf") for _ in range(N)]
cur[S] = V
for _ in range(N-1):
    for i in range(N):
        for j in range(N):
            if not graph[i][j]:
                continue
            r,c = graph[i][j]
            if cur[i] != -float('inf') and (cur[i]-c)*r > cur[j]:
                cur[j] = (cur[i]-c)*r
def check():
    for i in range(N):
        for j in range(N):
            if not graph[i][j]:
                continue
            r,c = graph[i][j]
            if cur[i] != -float('inf') and (cur[i]-c)*r > cur[j]:
                return False
    return True
if check():
    print("NO")
else:
    print("YES")