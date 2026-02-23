class Solution:
    def productExceptSelf(self, nums):
        if 0 in nums:
            a = nums.index(0)
            product = 1
            for i in range(len(nums)):
                if i != a:
                    product *= nums[i]
            return [0]*(a)+[product]+[0]*(len(nums)-a-1)
        import math
        total = 0
        fu = 0
        for num in nums:
            if num < 0:
                fu += 1
                fu %= 2
            total += math.log10(abs(num))
        print(fu,total)
        if fu:
            return [round(-10**(total-math.log10(abs(nums[i])))) if nums[i] > 0 else round(10**(total-math.log10(abs(nums[i])))) for i in range(len(nums))]
        return [round(10**(total-math.log10(abs(nums[i])))) if nums[i] > 0 else round(-10**(total-math.log10(abs(nums[i])))) for i in range(len(nums))]
print(Solution().productExceptSelf([1,-1]))