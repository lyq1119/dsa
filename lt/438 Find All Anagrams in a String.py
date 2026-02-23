from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str):
        result = []
        mydict = Counter(p)
        if len(s) < len(p):
            return result
        mydict1 = Counter(s[:len(p)])
        for i in range(len(s)-len(p)+1):
            if mydict1 == mydict:
                result.append(i)
            mydict1[s[i]] -= 1
            if i != len(s)-len(p):
                if mydict1[s[i]] == 0:
                    del mydict1[s[i]]
                mydict1[s[i+len(p)]] += 1
        return result
print(Solution().findAnagrams("abcabcabc","abc"))