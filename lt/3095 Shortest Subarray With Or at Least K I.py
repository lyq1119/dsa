class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        a = max(nums)
        if a >= k:
            return 1
        str1,str2 = bin(a)[2:],bin(k)[2:]
        if len(str1) < len(str2):
            return -1
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for t in range(n):
            dp[t][t] = nums[t]
        for cha in range(1,n):
            for i in range(n-cha):
                dp[i][i+cha] = dp[i][i+cha-1]|dp[i+cha][i+cha]
                if dp[i][i+cha] >= k:
                    return cha+1
        return -1
print(Solution().minimumSubarrayLength([1,2],0))
            