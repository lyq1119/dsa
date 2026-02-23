class Solution:
    def findDuplicate(self, nums) -> int:
        piv = 0
        for num in nums:
            cur = piv
            piv = piv|(1<<num)
            if piv == cur:
                return num