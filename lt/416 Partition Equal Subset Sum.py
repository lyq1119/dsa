class Solution:
    def canPartition(self, nums) -> bool:
        mysum = sum(nums)
        if mysum % 2 != 0:
            return False
        mysum //= 2
        dp = [0]*(mysum+1)
        for num in nums:
            for i in range(mysum,-1,-1):
                if i < num:
                    break
                if dp[i-num]:
                    dp[i] = 1
        if dp[-1]:
            return True
        return False