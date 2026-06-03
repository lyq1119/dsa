from typing import List
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0 for _ in range(n)]
        from collections import defaultdict
        pre_max = [0 for _ in range(n)]
        suf_min = [0 for _ in range(n)]
        for i in range(n):
            if i >= 1:
                pre_max[i] = max(pre_max[i-1],nums[i])
            else:
                pre_max[i] = nums[0]
        for i in range(n-1,-1,-1):
            if i < n-1:
                suf_min[i] = min(suf_min[i+1],nums[i])
            else:
                suf_min[i] = nums[-1]
        begin,end = 0,0
        for i in range(n):
            if i == 0:
                if suf_min[i+1] >= nums[i]:
                    res[0] = nums[0]
                continue
            if i == n-1:
                if pre_max[i-1] <= nums[i]:
                    res[i] = nums[i]
                    continue
                end = i
                for j in range(begin,end+1):
                    res[j] = pre_max[i]
                continue
            if pre_max[i-1] <= suf_min[i+1] and nums[i] < pre_max[i-1]:
                end = i
                for j in range(begin,end+1):
                    res[j] = pre_max[i]
            elif pre_max[i-1] <= suf_min[i+1] and nums[i] > suf_min[i+1]:
                begin,end = i,i
            elif pre_max[i-1] <= suf_min[i+1]:
                res[i] = nums[i]
            else:
                end = i
        return res
print(Solution().maxValue([2,1,3]))