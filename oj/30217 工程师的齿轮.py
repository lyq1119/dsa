def solve():
    n,t = map(int,input().split())
    mylist = list(map(int,input().split()))
    mydict = {}
    avai = []
    for i,num in enumerate(mylist):
        if t-num in mydict:
            avai.append((mydict[t-num]+1,i+1))
        if num not in mydict:
            mydict[num] = i
    avai.sort()
    print(avai[0][0],avai[0][1])
solve()   