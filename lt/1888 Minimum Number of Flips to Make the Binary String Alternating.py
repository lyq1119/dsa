class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        q0 = [0]*n
        q1 = [0]*n
        h0 = [0]*n
        h1 = [0]*n
        for i in range(n):
            if i == 0:
                if s[i] == "0":
                    q1[i] = 1
                else:
                    q0[i] = 1
                if s[-i-1] == "0":
                    h1[-i-1] = 1
                else:
                    h0[-i-1] = 1
            else:
                if s[i] == "0":
                    q1[i] = 1+q0[i-1]
                    q0[i] = q1[i-1]
                else:
                    q1[i] = q0[i-1]
                    q0[i] = 1+q1[i-1]
                if s[-i-1] == "0":
                    h1[-i-1] = 1+h0[-i]
                    h0[-i-1] = h1[-i]
                else:
                    h1[-i-1] = h0[-i]
                    h0[-i-1] = 1+h1[-i]
        if n%2 == 0:
            return min(q0[-1],q1[-1])
        if n == 1:
            return 0
        mymin = min(q0[-1],q1[-1])
        mymin = min(mymin,min(abs(int(s[0]))+abs(int(s[1]))+h1[2],abs(int(s[0])-1)+abs(int(s[1])-1)+h0[2]))
        mymin = min(mymin,min(abs(int(s[-1]))+abs(int(s[-2]))+q1[-3],abs(int(s[-1])-1)+abs(int(s[-2])-1)+q0[-3]))
        for i in range(1,n-2):
            mymin = min(mymin,abs(int(s[i]))+abs(int(s[i+1]))+q1[i-1]+h1[i+2])
            mymin = min(mymin,abs(int(s[i])-1)+abs(int(s[i+1])-1)+q0[i-1]+h0[i+2])
        return mymin             
print(Solution().minFlips("01001001101"))