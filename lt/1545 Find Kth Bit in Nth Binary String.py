class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def dfs(t,k):
            print(t,k)
            if t == 1:
                return 0
            if k == (1<<(t-1))-1:
                return 1
            if k < (1<<(t-1))-1:
                return dfs(t-1,k)
            return (dfs(t-1,(1<<t)-2-k)+1)%2
        return str(dfs(n,k-1))
print(Solution().findKthBit(4,12))