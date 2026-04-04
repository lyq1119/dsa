import sys
data = iter(sys.stdin.read().split())
times = int(next(data))
def huanyou(p,q):
    begin = (0,0)
    visited = {(0,0)}
    vectors = [(-1,-2),(1,-2),(-2,-1),(2,-1),(-2,1),(2,1),(-1,2),(1,2)]
    prev = {begin:None}
    result = []
    def backtrack(i,j):
        if len(visited) == p*q:
            cur = (i,j)
            while prev[cur]:
                result.append(cur)
                cur = prev[cur]
            result.append(begin)
            return True
        for a,b in vectors:
            if (i+a,j+b) not in visited and i+a >= 0 and i+a <= p-1 and j+b >= 0 and j+b <= q-1:            
                visited.add((i+a,j+b))
                prev[(i+a,j+b)] = (i,j)
                verdict = backtrack(i+a,j+b)
                if verdict:
                    return True
                visited.discard((i+a,j+b))
                del prev[(i+a,j+b)]
        return False
    backtrack(0,0)
    if not result:
        print("impossible")
        return
    for index in range(p*q):
        i,j = result[-index-1]
        if index != p*q-1:
            print(f"{chr(65+j)}{i+1}",end="")
        else:
            print(f"{chr(65+j)}{i+1}")
for i in range(times):
    p = int(next(data))
    q = int(next(data))
    print(f"Scenario #{i+1}:")
    huanyou(p,q)
    if i == times-1:
        break
    print("")
