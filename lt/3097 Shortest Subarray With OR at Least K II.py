class Solution:
    def minimumSubarrayLength(self, nums, k: int) -> int:
        i,j = 0,0
        minlength = len(nums)+1
        from functools import lru_cache
        def cal(mylist):
            total = 0
            for i in range(1,33):
                if mylist[-i]:
                    total += (1<<(i-1))
            return total
        @lru_cache(maxsize=None)
        def store(m):
            mylist = [int(s) for s in bin(nums[m])[2:]]
            for _ in range(32-len(mylist)):
                mylist.insert(0,0)
            return mylist
        mylist = store(0)
        def add(mylist1,mylist2):
            return [mylist1[i]+mylist2[i] for i in range(32)]
        def subtract(mylist1,mylist2):
            return [mylist1[i]-mylist2[i] for i in range(32)]
        while j <= len(nums)-1:
            a = cal(mylist)
            if a >= k:
                minlength = min(minlength,j-i+1)
                if i+1 <= j:
                    mylist1 = subtract(mylist,store(i))
                    if cal(mylist1) >= k:
                        mylist = mylist1
                        i += 1
                    elif j+1 <= len(nums)-1:
                        mylist = add(mylist,store(j+1))
                        j += 1
                    else:
                        j += 1
                elif j+1 <= len(nums)-1:
                    mylist = add(mylist,store(j+1))
                    j += 1
                else:
                    j += 1
            elif j+1 <= len(nums)-1:
                mylist = add(mylist,store(j+1))
                j += 1
            else:
                j += 1
        if minlength == len(nums)+1:
            return -1
        else:
            return minlength
print(Solution().minimumSubarrayLength([4,3,3,8],11))