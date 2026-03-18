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
    return lps
i = 1
flag = True
while True:
    n = int(next(data))
    if n == 0:
        break
    s = next(data)
    print(f"Test case #{i}")
    lps = kmp(s)
    for t in range(1,n+1):
        jie = t-lps[t-1]
        if t%jie == 0 and t!=jie:
            print(t,t//jie)
    print("")
    i += 1