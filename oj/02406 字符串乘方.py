import sys
data = iter(sys.stdin.readlines())
def kmp(s):
    j = 0
    n = len(s)-1
    lps = [0]*n
    for i in range(1,n):
        while j > 0 and s[j] != s[i]:
            j = lps[j-1]
        if s[j] == s[i]:
            j += 1
        lps[i] = j
    jie = n-lps[n-1]
    if n%jie == 0:
        return n//jie
    return 1
while True:
    s = next(data)
    if s[0] == ".":
        break
    print(kmp(s))