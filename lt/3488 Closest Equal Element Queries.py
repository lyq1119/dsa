from typing import List
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        from collections import defaultdict
        from bisect import bisect_left
        mydict = defaultdict(list)
        for i,num in enumerate(nums):
            mydict[num].append(i)
        result = []
        for j in queries:
            num = nums[j]
            distribution = mydict[num]
            if len(distribution) == 1:
                result.append(-1)
                continue
            t = bisect_left(distribution,j)
            if t == len(distribution)-1:
                result.append(min(distribution[0]+len(nums)-distribution[t],distribution[t]-distribution[t-1]))
                continue
            if t == 0:
                result.append(min(distribution[t+1]-distribution[t],distribution[t]+len(nums)-distribution[t-1]))
                continue
            result.append(min(distribution[t+1]-distribution[t],distribution[t]-distribution[t-1]))
        return result
print(Solution().solveQueries([1,3,1,4,1,3,2],[0,3,5]))