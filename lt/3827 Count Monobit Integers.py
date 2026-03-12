class Solution:
    def countMonobit(self, n: int) -> int:
        import math
        return int(math.log2(n+1))+1