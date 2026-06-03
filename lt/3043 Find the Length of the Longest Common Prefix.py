class Trie:
    def __init__(self):
        self.tree = {}  
    def insert(self, word: str) -> None:
        cur = self.tree  
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        # 单词结束标记（用 None 表示结尾）
        cur[None] = True
    def startsWith(self, prefix: str) -> bool:
        cur = self.tree
        count = 0
        for c in prefix:
            if c not in cur:
                return count
            cur = cur[c]
            count += 1
        return count
class Solution:
    def longestCommonPrefix(self, arr1, arr2) -> int:
        tree = Trie()
        for num in arr1:
            tree.insert(str(num))
        mymax = 0
        for num in arr2:
            mymax = max(mymax,tree.startsWith(str(num)))
        return mymax
        