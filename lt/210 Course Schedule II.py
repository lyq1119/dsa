from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import deque, defaultdict
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)
        def has_cycle_karn(graph,n): # n是顶点数
            res = []
            indegree = [0] * n
            num_visited = 0
            queue = deque()
            # 计算每个顶点的入度
            for u in graph:
                for v in graph[u]:
                    indegree[v] += 1
            # 将入度为 0 的顶点加入队列
            for u in range(n):
                if indegree[u] == 0:
                    queue.append(u)
            # 执行拓扑排序
            while queue:
                u = queue.popleft()
                res.append(u)
                num_visited += 1
                for v in graph[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        queue.append(v)
            return num_visited != n,res
        verdict = has_cycle_karn(graph,numCourses)
        if verdict[0]:
            return []
        else:
            return verdict[1]
print(Solution().findOrder(4,[[1,0],[3,0],[2,1],[2,3]]))