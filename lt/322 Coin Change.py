class Solution:
    def coinChange(self, coins, amount: int) -> int:
        if not amount:
            return 0
        coins.sort()
        from collections import deque
        dp = [0]*(amount+1)
        queue = deque([0])
        while queue:
            t = queue.popleft()
            for coin in coins:
                if t+coin > amount:
                    continue
                if dp[t+coin]:
                    continue
                dp[t+coin] = dp[t]+1
                queue.append(t+coin)
        if dp[-1]:
            return dp[-1]
        return -1