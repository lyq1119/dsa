from collections import defaultdict
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        Parent = [i for i in range(n)]
        def find(i):
            if (Parent[i] == i):
                return i
            else:
                result = find(Parent[i])
                Parent[i] = result
                return result
        def union(i,j):
            i1 = find(i)
            j1 = find(j)
            Parent[j1] = i1
        for i,j in allowedSwaps:
            union(i,j)
        Parent = [find(i) for i in range(n)]
        mydict = defaultdict(list)
        for i,item in enumerate(Parent):
            mydict[item].append(i)
        total = 0
        for value in mydict.values():
            cdict1 = defaultdict(int)
            cdict2 = defaultdict(int)
            for num in value:
                cdict1[target[num]] += 1
                cdict2[source[num]] += 1
            for key,val in cdict2.items():
                total += min(val,cdict1[key])
        return n-total