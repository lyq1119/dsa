from collections import deque, defaultdict

def karn(graph,n): # n是顶点数
    verdict = True
    indegree = [0] * n
    result = []
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
        if len(queue) != 1:
            verdict = False
        u = queue.popleft()
        result.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    return result,verdict

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def solve():
    res,verdict = karn(graph,n)
    if len(res) != n:
        print("Device error.")
        return 
    if not verdict:
        print("Not determined.")
        return
    i = 0
    def build(pos):
        nonlocal i
        if pos >= n:
            i -= 1
            return
        node = TreeNode(res[i])
        i += 1
        node.right = build(2*pos+2)
        i += 1
        node.left = build(2*pos+1)
        return node
    root = build(0)
    res = []
    def inorder(node):
        if node:
            inorder(node.left)
            res.append(node.val+1)
            inorder(node.right)
    inorder(root)
    print(*res)

if __name__ == "__main__":
    n,m = map(int,input().split())
    graph = defaultdict(set)
    for _ in range(m):
        a,__,b = input().split()
        a = int(a)-1
        b = int(b)-1
        graph[a].add(b)
    solve()