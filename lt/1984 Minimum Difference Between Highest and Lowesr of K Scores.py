class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        mymin = float("inf")
        for i in range(len(nums)-k+1):
            mymin = min(nums[i+k-1]-nums[i],mymin)
        return mymin