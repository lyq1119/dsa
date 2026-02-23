from itertools import product
from typing import List

class Solution:
    INF = 1 << 30

    def solve(self) -> None:
        n = int(input())
        locations = [input().strip() for _ in range(n)]

        distances = [[self.INF] * n for _ in range(n)]
        next_node = [[-1] * n for _ in range(n)]

        # 初始化自身到自身的距离为 0
        for i in range(n):
            distances[i][i] = 0

        # 读取边信息并初始化邻接矩阵和路径表
        for _ in range(int(input())):
            a, b, d = input().split()
            u, v, dist = locations.index(a), locations.index(b), int(d)
            if dist < distances[u][v]:
                distances[u][v] = distances[v][u] = dist
                next_node[u][v] = v
                next_node[v][u] = u

        # Floyd-Warshall 算法计算所有点对最短路径
        for k, i, j in product(range(n), repeat=3): # 产生所有可能的i, j, k组合
            if distances[i][j] > distances[i][k] + distances[k][j]:
                distances[i][j] = distances[i][k] + distances[k][j]
                next_node[i][j] = next_node[i][k]

        # 查询路径
        for _ in range(int(input())):
            a, b = input().split()
            u, v = locations.index(a), locations.index(b)
            if distances[u][v] == self.INF:
                print("No path")
            else:
                print(self.reconstruct_path(next_node, u, v, locations, distances))

    def reconstruct_path(self, next_node: List[List[int]],
                         u: int, v: int, locations: List[str], distances: List[List[int]]) -> str:
        path_indices = [u]
        while u != v:
            u = next_node[u][v]
            path_indices.append(u)

        # 构造格式化路径字符串
        result = locations[path_indices[0]]
        for i in range(1, len(path_indices)):
            from_idx, to_idx = path_indices[i - 1], path_indices[i]
            result += f"->({distances[from_idx][to_idx]})->{locations[to_idx]}"
        return result

if __name__ == "__main__":
    Solution().solve()
