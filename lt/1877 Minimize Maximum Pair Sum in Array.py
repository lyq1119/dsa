class Solution:
    def minPairSum(self, nums) -> int:
        nums.sort()
        mymax = 0
        for i in range(len(nums)//2):
            mymax = max(mymax,nums[i]+nums[-i-1])
        return mymax