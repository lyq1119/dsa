class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        n = len(nums1)
        m = len(nums2)
        def fun(i,j):
            if i == n:
                return i,j+1,nums2[j]
            if j == m:
                return i+1,j,nums1[i]
            if nums1[i] < nums2[j]:
                return i+1,j,nums1[i]
            return i,j+1,nums2[j]
        t = 1
        if (m+n)%2 == 0:
            cur1,cur2 = 0,0
            while True:
                if t == (m+n)//2:
                    cur1,cur2,val1 = fun(cur1,cur2)
                elif t == (m+n)//2+1:
                    cur1,cur2,val2 = fun(cur1,cur2)
                    break
                else:
                    cur1,cur2,val = fun(cur1,cur2)
                t += 1
            return (val1+val2)/2
        else:
            cur1,cur2 = 0,0
            while True:
                if t == (m+n)//2+1:
                    cur1,cur2,val2 = fun(cur1,cur2)
                    return val2
                else:
                    cur1,cur2,val = fun(cur1,cur2)
                t += 1
print(Solution().findMedianSortedArrays([2],[1]))
        