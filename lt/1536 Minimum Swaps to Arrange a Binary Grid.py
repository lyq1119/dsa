import math
class Solution:
    def minSwaps(self, grid) -> int:
        n = len(grid)
        result = []
        count = 0
        for row in grid:
            t = "".join([str(num) for num in row])
            s = int(t,2)
            if s:
                result.append(int(math.log2(s&(-s))))
            else:
                result.append(n)
        for i in range(n):
            if result[i] < n-i-1:
                flag = False
                for j in range(i+1,n):
                    if result[j] >= n-i-1:
                        flag = True
                        break
                if not flag:
                    return -1
                count += (j-i)
                t = result.pop(j)
                result.insert(i,t)
        return count
print(Solution().minSwaps([[0,0,1],[1,1,0],[1,0,0]]))