class Solution:
    def allPathsSourceTarget(self, graph):
        visited = set()
        result = []
        mylist = []
        def dfs(i):
            print(i)
            mylist.append(i)
            visited.add(i)
            if i == len(graph)-1:
                result.append(mylist.copy())
            else:
                for t in graph[i]:
                    if t not in visited:
                        dfs(t)
            mylist.pop()
            visited.discard(i)
        dfs(0)
        return result
print(Solution().allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))