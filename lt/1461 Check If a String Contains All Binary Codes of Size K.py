class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool: 
        if len(s) < k:
            return False
        storage = set()
        curstr = [s[j] for j in range(k-1)]
        for i in range(len(s)-k+1):
            curstr.append(s[i+k-1])
            storage.add("".join(curstr))
            curstr.pop(0)
        if len(storage) == (1<<k):
            return True
        return False
print(Solution().hasAllCodes("00110",2)) 
