class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        from bisect import bisect_left
        cur = []
        for num in nums:
            a = bisect_left(cur,num)
            if a >= len(cur):
                cur.append(num)
            else:
                cur[a] = num
        return len(nums)