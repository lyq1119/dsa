class Solution:
    def largestSquareArea(self, bottomLeft, topRight) -> int:
        def check(i1,j1,k1,l1,i2,j2,k2,l2):
            mymax = float('inf')
            if i1 > i2:
                i1,j1,k1,l1,i2,j2,k2,l2 = i2,j2,k2,l2,i1,j1,k1,l1
            if k1 <= i2:
                return 0
            else:
                mymax = min(mymax,k1-i2)
            if j1 > j2:
                i1,j1,k1,l1,i2,j2,k2,l2 = i2,j2,k2,l2,i1,j1,k1,l1
            if l1 <= j2:
                return 0
            else:
                mymax = min(mymax,l1-j2)
            return mymax
        mymax = 0
        for i in range(len(bottomLeft)):
            for j in range(i+1,len(bottomLeft)):
                mymax = max(mymax,check(bottomLeft[i][0],bottomLeft[i][1],topRight[i][0],topRight[i][0],bottomLeft[j][0],bottomLeft[j][1],topRight[j][0],topRight[j][0]))
        return mymax**2
print(Solution().largestSquareArea([[1,1],[3,3],[3,1]],[[2,2],[4,4],[4,2]]))