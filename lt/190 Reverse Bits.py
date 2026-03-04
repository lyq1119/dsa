class Solution:
    def reverseBits(self, n: int) -> int:
        t = bin(n)[2:][::-1]
        s = 32 - len(t)
        m = 0
        for i in range(1,len(t)+1):
            m += int(t[-i])*(2**(i-1))
        return m*(2**s)
print(Solution().reverseBits(43261596))