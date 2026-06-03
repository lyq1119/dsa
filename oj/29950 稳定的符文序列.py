s = list(input())
n = len(s)
maxlength = 1
myset = {s[0]}
l,r = 0,0
while r+1 < n:
    if s[r+1] not in myset:
        r += 1
        myset.add(s[r])
        maxlength = max(maxlength,r-l+1)
    else:
        while s[l] != s[r+1]:
            myset.discard(s[l])
            l += 1
        l += 1
        r += 1
        maxlength = max(maxlength,r-l+1)
print(maxlength)