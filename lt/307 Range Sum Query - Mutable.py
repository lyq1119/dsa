from itertools import accumulate
class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.shuzhuangshuzu = [0 for _ in range(len(nums)+1)]
        qianzhuihe = [0]+list(accumulate(self.nums))
        for i in range(1,len(nums)+1):
            lowbit = i&(-i)
            self.shuzhuangshuzu[i] = qianzhuihe[i]-qianzhuihe[i-lowbit]
    def update(self, index: int, val: int) -> None:
        a = val-self.nums[index]
        self.nums[index] = val
        index += 1
        while index <= len(self.nums):
            self.shuzhuangshuzu[index] += a
            index += (index&(-index))
    def sumRange(self, left: int, right: int) -> int:
        def calsum(i):
            total = 0
            while i:
                total += self.shuzhuangshuzu[i]
                i -= (i&(-i))
            return total
        return calsum(right+1)-calsum(left)