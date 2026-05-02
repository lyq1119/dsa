class Solution:
    def maxStability(self, n: int, edges, k: int) -> int:
        import heapq # 每次弹最大的
        import math
        Parent = [i for i in range(n)]
        def find(i):
            if i == Parent[i]:
                return i
            else:
                result = find(Parent[i])
                Parent[i] = result
                return result
        def union(i,j):
            i1 = find(i)
            j1 = find(j)
            if i1 == j1:
                return True
            Parent[j1] = i1
            return False
        heap = []
        mymin = float("inf")
        resedges = n-1
        mylist = []
        for edge in edges:
            if edge[-1] == 1:
                a,b = edge[0],edge[1]
                if union(a,b):
                    return -1
                mymin = min(mymin,edge[2])
                resedges -= 1
            else:
                heapq.heappush(heap,(-edge[2],edge[0],edge[1]))
        while resedges and heap:
            a,b,c = heapq.heappop(heap)
            if find(b) == find(c):
                continue
            mylist.append(-a)
            union(b,c)
            resedges -= 1
        if resedges:
            return -1
        if 0 in mylist:
            return 0
        if mymin != float("inf"):
            left,right = 0,mymin
        else:
            left,right = 0,(10**5)*2*2
        def check(t):
            if t == 0:
                return True
            if t > mymin:
                return False
            total = 0
            for num in mylist:
                if num >= t:
                    continue
                if num < t/2:
                    return False
                total += 1
                if total > k:
                    return False
            return True
        while left <= right:
            if left == right:
                if check(left):
                    return left
                else:
                    return -1
            mid = (left+right)//2
            if check(mid):
                left = mid
            else:
                right = mid-1
            if right-left == 1:
                if check(right):
                    return right
                if check(left):
                    return left
                return -1
print(Solution().maxStability(3,[[0,1,1,1],[1,2,1,1],[2,0,1,1]],0))
            



        