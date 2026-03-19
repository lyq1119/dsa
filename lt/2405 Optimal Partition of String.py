class Solution:
    def partitionString(self, s: str) -> int:
        myset = set()
        count = 1
        for i in range(len(s)):
            t = s[i]
            origin = len(myset)
            myset.add(t)
            if len(myset) == origin:
                myset = {t}
                count += 1
        return count
