from itertools import accumulate
class NumArray:

    def __init__(self, nums: List[int]):
        self.mylist = list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.mylist[right]
        return self.mylist[right] - self.mylist[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)