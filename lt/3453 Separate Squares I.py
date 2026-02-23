class Solution:
    def separateSquares(self, squares) -> float:
        bottom,top = 0,2*(10**9)
        n = len(squares)
        total1 = sum([(squares[i][-1])**2 for i in range(n)])
        def check(l,total1):
            total = 0
            for a,b,c in squares:
                if b < l:
                    if b+c > l:
                        total += c*(l-b)
                    else:
                        total += c**2
            if total >= (total1/2):
                return True
            return False
        while bottom <= top:
            mid = (bottom+top)/2
            status = check(mid,total1)
            print(status,bottom,top)
            if top - bottom <= 10**(-5):
                return mid
            if status:
                top = mid
            else:
                bottom = mid
print(Solution().separateSquares([[0,0,1],[2,2,1]]))
                
