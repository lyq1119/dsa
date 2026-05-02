class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        from collections import defaultdict
        mydict1 = defaultdict(int)
        mydict2 = defaultdict(int)
        mydict3 = defaultdict(int)
        mydict4 = defaultdict(int)
        for i in range(len(s1)):
            if i % 2 == 0:
                mydict1[s1[i]] += 1
            else:
                mydict2[s1[i]] += 1
        for j in range(len(s2)):
            if j % 2 == 0:
                mydict3[s2[j]] += 1
            else:
                mydict4[s2[j]] += 1
        if mydict1 == mydict3 and mydict2 == mydict4:
            return True
        return False