from collections import defaultdict
class Solution:
    def sortByBits(self, arr):
        arr.sort()
        mylist = []
        mydict = defaultdict(list)
        for num in arr:
            t = bin(num).count("1")
            mydict[t].append(num)
        for s in sorted(list(mydict)):
            mylist.extend(mydict[s])
        return mylist
print(Solution().sortByBits([0,1,2,3,4,5,6,7,8]))