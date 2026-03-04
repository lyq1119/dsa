class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [-1]*n
        for i in range(1,n):
            if s[i] != ")":
                continue
            if s[i-1] == "(":
                dp[i] = i-1
            else:
                if dp[i-1] == -1:
                    continue
                if dp[i-1] == 0:
                    continue
                if s[dp[i-1]-1] == "(":
                    dp[i] = dp[i-1]-1
            j = dp[i]
            if j >= 1 and dp[j-1] != -1:
                dp[i] = dp[j-1]
        mymax = 0
        for i in range(n):
            if dp[i] >= 0:
                mymax = max(mymax,i-dp[i]+1)
        return mymax
print(Solution().longestValidParentheses(")(((((()())()()))()(()))("))

