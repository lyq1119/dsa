from collections import defaultdict
n = int(input())
mydictM = defaultdict(list)
mydictB = defaultdict(list)
moxinglist = set()
for _ in range(n):
    moxing,canshu = input().split("-")
    moxinglist.add(moxing)
    if canshu[-1] == "B":
        mydictB[moxing].append(canshu)
    else:
        mydictM[moxing].append(canshu)
moxinglist = list(moxinglist)
moxinglist.sort()
for key in moxinglist:
    Mlist = mydictM[key]
    Blist = mydictB[key]
    mytuplesM = [(float(canshu[:-1]),canshu) for canshu in Mlist]
    mytuplesB = [(float(canshu[:-1]),canshu) for canshu in Blist]
    mytuplesM.sort()
    mytuplesB.sort()
    mystring = key+": "
    mystring += ", ".join([yuanzu[1] for yuanzu in mytuplesM])
    if mytuplesM and mytuplesB:
        mystring += ", "
    mystring += ", ".join([yuanzu[1] for yuanzu in mytuplesB])
    print(mystring)