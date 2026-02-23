import math
class Solution:
    def minBitwiseArray(self, nums):
        for i in range(len(nums)):
            s = nums[i]
            if s == 2:
                nums[i] = -1
            else:
                a = int(math.log2(((~(s+1))&s)+1))-1
                nums[i] = s&(~(1<<a))
        return nums
print(Solution().minBitwiseArray([2,3,5,7,11,13,31]))

