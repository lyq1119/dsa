import sys
import heapq
def merge(mylist1,mylist2,n):
    mylist = []
    stack = [(mylist1[0]+mylist2[0],0,0)]
    visited = {(0,0)}
    for t in range(n):
        a,i,j = heapq.heappop(stack)
        mylist.append(a)
        if i < n-1 and (i+1,j) not in visited:
            heapq.heappush(stack,(mylist1[i+1]+mylist2[j],i+1,j))
            visited.add((i+1,j))
        if j < n-1 and (i,j+1) not in visited:
            heapq.heappush(stack,(mylist1[i]+mylist2[j+1],i,j+1))
            visited.add((i,j+1))
    return mylist
input_data = sys.stdin.read().split()
it = iter(input_data)
T = int(next(it))
for _ in range(T):
    m = int(next(it))
    n = int(next(it))
    current = sorted(int(next(it)) for _ in range(n))
    for _ in range(m - 1):
        seq = sorted(int(next(it)) for _ in range(n))
        current = merge(current, seq,n)
    print(*current)
                    



   



