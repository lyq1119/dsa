from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        from collections import deque,defaultdict
        n = len(edges)
        graph = defaultdict(list)
        for a,b in edges:
            a -= 1
            b -= 1
            graph[a].append(b)
            graph[b].append(a)
        def karn(graph,n): # n是顶点数
            degree = [0] * n
            result = set()
            queue = deque()
            # 计算每个顶点的入度
            for u in graph:
                for v in graph[u]:
                    degree[v] += 1
            # 将入度为 0 的顶点加入队列
            for u in range(n):
                if degree[u] == 1:
                    queue.append(u)
            # 执行拓扑排序
            while queue:
                u = queue.popleft()
                result.add(u)
                for v in graph[u]:
                    degree[v] -= 1
                    if degree[v] == 1:
                        queue.append(v)
            return result
        result = karn(graph,n)
        circle = {i for i in range(n) if i not in result}
        i,j = 0,0
        for a,b in edges:
            if a-1 in circle and b-1 in circle:
                i,j = a,b
        return [i,j]