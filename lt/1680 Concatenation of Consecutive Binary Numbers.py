class Solution:
    def concatenatedBinary(self, n: int) -> int:
        zhi = 0
        ermi = 1
        for t in range(n,0,-1):
            zhi += ermi*t
            zhi %= (10**9+7)
            ermi *= ((2**(len(bin(t))-2))%(10**9+7))
            ermi %= (10**9+7)
        return zhi
print(Solution().concatenatedBinary(72387))