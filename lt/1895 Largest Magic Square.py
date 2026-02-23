class Solution:
    def largestMagicSquare(self, grid) -> int:
        m,n = len(grid),len(grid[0])
        t = min(m,n)
        hangqianzhuihe = [[0]*(n+1) for _ in range(m)]
        lieqianzhuihe = [[0]*(m+1) for _ in range(n)]
        for i in range(m):
            for j in range(1,n+1):
                hangqianzhuihe[i][j] = hangqianzhuihe[i][j-1] + grid[i][j-1]
        for i in range(n):
            for j in range(1,m+1):
                lieqianzhuihe[i][j] = lieqianzhuihe[i][j-1] + grid[j-1][i]
        def check(s,i,j):
            pivot = hangqianzhuihe[i][j+s] - hangqianzhuihe[i][j]
            for k in range(i,i+s):
                if pivot != hangqianzhuihe[k][j+s] - hangqianzhuihe[k][j]:
                    return False
            for k in range(j,j+s):
                if pivot != lieqianzhuihe[k][i+s] - lieqianzhuihe[k][i]:
                    return False
            duijiaoxian1 = sum([grid[i+l][j+l] for l in range(s)])
            if duijiaoxian1 != pivot:
                return False
            duijiaoxian2 = sum([grid[i+l][j+s-1-l] for l in range(s)])
            if duijiaoxian2 != pivot:
                return False
            return True
        for s in range(t,0,-1):
            for i in range(m-s+1):
                for j in range(n-s+1):
                    if check(s,i,j):
                        return s
print(Solution().largestMagicSquare([[5,1,3,1],[9,3,3,1],[1,3,3,8]]))