class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 1
        myset = {0}
        for i in range(1,len(s)):
            myset1 = myset.copy()
            myset = {i}
            if s[i] == s[i-1]:
                myset.add(i-1)
            for t in myset1:
                if t > 0 and s[t-1] == s[i]:
                    myset.add(t-1)
            count += len(myset)
        return count
        