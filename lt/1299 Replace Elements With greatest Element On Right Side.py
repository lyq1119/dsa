class Solution:
    def replaceElements(self, arr):
        cur = arr[-1]
        cun = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2,-1,-1):
            cur = max(cun,cur)
            cun = arr[i]
            arr[i] = cur
        return arr
print(Solution().replaceElements([17,18,5,4,6,1]))
