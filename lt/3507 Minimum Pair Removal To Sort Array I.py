class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0
        while nums != sorted(nums):
            count += 1
            store = []
            for i in range(len(nums)-1):
                store.append(nums[i]+nums[i+1])
            a = store.index(min(store))
            nums1 = []
            for i in range(len(nums)):
                if i < a:
                    nums1.append(nums[i])
                elif i == a:
                    nums1.append(store[i])
                elif i == a+1:
                    continue
                else:
                    nums1.append(nums[i])
            nums = nums1
        return count