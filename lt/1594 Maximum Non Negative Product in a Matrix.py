class Solution:
    def maxProductPath(self, grid) -> int:
        if grid[-1][-1] == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[[-float("inf"),float("inf")] for _ in range(n)] for __ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                if i == 0 and j == 0:
                    if grid[i][j] > 0:
                        dp[i][j][0] = grid[i][j]
                    else:
                        dp[i][j][1] = grid[i][j]
                flag = True
                if i != 0:
                    if grid[i-1][j] == 0:
                        flag = False
                    if flag:
                        t,s = dp[i-1][j]
                        if grid[i][j] > 0:
                            if t != -float("inf"):
                                dp[i][j][0] = max(dp[i][j][0],t*grid[i][j])
                            if s != float("inf"):
                                dp[i][j][1] = min(dp[i][j][1],s*grid[i][j])
                        else:
                            if t != -float("inf"):
                                dp[i][j][1] = min(dp[i][j][1],t*grid[i][j])
                            if s != float("inf"):
                                dp[i][j][0] = max(dp[i][j][0],s*grid[i][j])
                if j != 0:
                    if grid[i][j-1] == 0:
                        continue
                    t,s = dp[i][j-1]
                    if grid[i][j] > 0:
                        if t != -float("inf"):
                            dp[i][j][0] = max(dp[i][j][0],t*grid[i][j])
                        if s != float("inf"):
                            dp[i][j][1] = min(dp[i][j][1],s*grid[i][j])
                    else:
                        if t != -float("inf"):
                            dp[i][j][1] = min(dp[i][j][1],t*grid[i][j])
                        if s != float("inf"):
                            dp[i][j][0] = max(dp[i][j][0],s*grid[i][j])
        if dp[-1][-1][0] == -float("inf"):
            for row in grid:
                if 0 in row:
                    return 0
            return -1
        return dp[-1][-1][0]%(10**9+7)
print(Solution().maxProductPath([[1,4,4,0],[-2,0,0,1],[1,-1,1,1]]))
        