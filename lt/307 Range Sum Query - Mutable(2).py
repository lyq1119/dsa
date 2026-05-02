from typing import List
import math
class NumArray:
    def __init__(self, nums: List[int]):
        n = 2**math.ceil(math.log2(len(nums)))
        self.tree = [0]*(2*n)
        for i in range(len(nums)):
            self.tree[n+i] = nums[i]
        for i in range(n-1,0,-1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
    def update(self, index: int, val: int) -> None:
        index = index+(len(self.tree)//2)
        difference = val-self.tree[index]
        while index != 0:
            self.tree[index] += difference
            index //= 2
    def sumRange(self, left: int, right: int) -> int:
        left += len(self.tree)//2
        right += len(self.tree)//2
        right += 1
        total = 0
        while left<right:
            if left % 2 != 0:
                total += self.tree[left]
                left += 1
            if right % 2 != 0:
                right -= 1
                total += self.tree[right]
            left //= 2
            right //= 2
        return total

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)