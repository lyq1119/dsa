class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        count = 0
        mystr = ""
        mylist = []
        def backtrack(n,t,k):
            nonlocal count
            nonlocal mystr
            if t == n:
                count += 1
                if count == k:
                    mystr = "".join(mylist)
                return 
            for w in ["a","b","c"]:
                if mylist and mylist[-1] == w:
                    continue
                mylist.append(w)
                backtrack(n,t+1,k)
                mylist.pop()
        backtrack(n,0,k)
        return mystr
print(Solution().getHappyString(3,1))