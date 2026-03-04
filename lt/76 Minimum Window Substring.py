class Solution:
    def minWindow(self, s, t):
        from collections import Counter, defaultdict

        mydict = Counter(t)
        count = defaultdict(int)
        available = set()
        b, e = 0, -1
        minlength = float("inf")
        i = -1
        j = -1

        while e < len(s):
            if len(available) < len(mydict):
                e += 1
                if e == len(s):
                    break
                if s[e] not in mydict:
                    continue
                count[s[e]] += 1
                if count[s[e]] >= mydict[s[e]]:
                    available.add(s[e])
            elif len(available) == len(mydict):
                if minlength > e - b + 1:
                    minlength = e - b + 1
                    i, j = b, e
                b += 1
                if s[b-1] not in mydict:
                    continue
                count[s[b-1]] -= 1
                if count[s[b-1]] < mydict[s[b-1]]:
                    available.discard(s[b-1])

        if i == -1:
            return ""
        return s[i:j+1]