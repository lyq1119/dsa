import math
class Solution:
    def firstMissingPositive(self, nums) -> int:
        t = 0
        for num in nums:
            if num <= 0:
                continue
            if num > len(nums):
                continue
            t = t|(1<<(num-1))
        t += 1
        return int(math.log2(t&(-t)))+1
print(Solution().firstMissingPositive([7,8,9,11,12]))