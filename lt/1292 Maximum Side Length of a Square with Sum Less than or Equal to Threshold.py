class Solution:
    def maxSideLength(self, mat, threshold: int) -> int:
        grid = mat
        m,n = len(grid),len(grid[0])
        t = min(m,n)
        qianzhuihe = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                qianzhuihe[i][j] = qianzhuihe[i][j-1] + sum([grid[k][j-1] for k in range(i)])
        def check(s,i,j):
            total = qianzhuihe[i+s][j+s] - qianzhuihe[i+s][j] - qianzhuihe[i][j+s] + qianzhuihe[i][j]
            return total
        for s in range(t,0,-1):
            mymin = float("inf")
            for i in range(m-s+1):
                for j in range(n-s+1):
                    mymin = min(check(s,i,j),mymin)
            if mymin <= threshold:
                return s
        return 0