class Solution:
    def numSteps(self, s: str) -> int:
        flag = True
        for i in range(1,len(s)):
            if s[i] == "1":
                flag = False
                break
        if flag:
            return len(s)-1
        for i in range(1,len(s)+1):
            if s[-i] == "1":
                break
        return len(s)+list(s).count("0")-i+2