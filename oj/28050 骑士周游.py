n = int(input())
x,y = map(int,input().split())
vector = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
def available(lc):
    mylist = []
    for myvector in vector:
        a,b = lc[0]+myvector[0],lc[1]+myvector[1]
        if a >= 0 and a <= n-1 and b >= 0 and b <= n-1:
            mylist.append((a,b))
    return mylist
def count(lc,myset):
    count = 0
    for t in available(lc):
        if t not in myset:
            count += 1
    return count
def choose(mylist,myset):
    mylist.sort(key=lambda x:count(x,myset))
    return mylist
def backtrack(lc,myset):
    if len(myset) == n*n:
        return True
    mylist = choose(available(lc),myset)
    for lc1 in mylist:
        if lc1 not in myset:
            myset.add(lc1)
            a = backtrack(lc1,myset)
            if a:
                myset.discard(lc1)
                return True
            myset.discard(lc1)
    return False
if backtrack((x,y),{(x,y)}):
    print("success")
else:
    print("fail")