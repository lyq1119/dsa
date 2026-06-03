class Solution:
    def minimumCost(self, target: str, words, costs) -> int:
        trie = {}
        for i in range(len(words)):
            word = words[i]
            cost = costs[i]
            cur = trie
            for char in word:
                if char not in cur:
                    cur[char] = {}
                    cur = cur[char]
                    continue
                cur = cur[char]
            if "E" in cur:
                cur["E"] = min(cur["E"],cost)
            else:
                cur["E"] = cost
        dp = [float("inf") for _ in range(len(target)+1)]
        dp[0] = 0
        for i in range(1,len(target)+1):
            if dp[i-1] == float("inf"):
                continue
            cur = trie
            for j in range(i-1,len(target)+1):
                if "E" in cur:
                    dp[j] = min(dp[j],dp[i-1]+cur["E"])
                if j == len(target):
                    break
                if target[j] not in cur:
                    break
                cur = cur[target[j]]
        return dp[-1] if dp[-1] != float("inf") else -1
print(Solution().minimumCost("abcdef",["abdef","abc","d","def","ef"],[100,1,1,10,5]))
"""class Solution:
    def minimumCost(self, target: str, words, costs) -> int:
        import sys
        INF = float('inf')
        n = len(target)
        
        # 1. 去重：相同单词保留最小花费
        word_cost = {}
        for w, c in zip(words, costs):
            if w not in word_cost or c < word_cost[w]:
                word_cost[w] = c
        
        # 2. 收集所有合法单词 + 长度集合
        words_unique = list(word_cost.keys())
        lenset = set(len(w) for w in words_unique)
        max_len = max(lenset) if lenset else 0
        
        # 3. DP
        dp = [INF] * (n + 1)
        dp[0] = 0
        
        for i in range(n):
            if dp[i] == INF:
                continue
            # 只遍历存在的单词长度，不逐个字符枚举
            for L in lenset:
                if i + L > n:
                    continue
                sub = target[i:i+L]
                if sub in word_cost:
                    if dp[i] + word_cost[sub] < dp[i+L]:
                        dp[i+L] = dp[i] + word_cost[sub]
        
        return dp[-1] if dp[-1] != INF else -1"""