class Solution:
    def binaryGap(self, n: int) -> int:
        s = bin(n)[2:]
        gap = 0
        begin = s.index("1")
        end = begin
        while end < len(s):
            if begin == end:
                end += 1
            elif s[end] != "1":
                end += 1
            elif s[end] == "1":
                gap = max(gap,end-begin)
                begin = end
        return gap