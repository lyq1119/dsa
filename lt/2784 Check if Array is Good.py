class Solution:
    def isGood(self, nums) -> bool:
        from collections import Counter
        mydict = Counter(nums)
        for i in range(1,len(nums)):
            if i not in nums:
                return False
        return max(nums) == len(nums)-1 and mydict[max(nums)] == 2