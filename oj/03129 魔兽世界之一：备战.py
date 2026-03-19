for t in range(1,int(input())+1):
    print(f"Case:{t}")
    M = int(input())
    M1 = M
    M2 = M
    mylist = list(map(int,input().split()))
    red = [("iceman",mylist[2]),("lion",mylist[3]),("wolf",mylist[4]),("ninja",mylist[1]),("dragon",mylist[0])]
    blue = [("lion",mylist[3]),("dragon",mylist[0]),("ninja",mylist[1]),("iceman",mylist[2]),("wolf",mylist[4])]
    minlife = min(mylist)
    flag1 = True
    flag2 = True
    time = 0
    i1 = 0
    i2 = 0
    list1 = [0,0,0,0,0]
    list2 = [0,0,0,0,0]
    while flag1 or flag2:
        if flag1:
            if M1 < minlife:
                flag1 = False
                print(f"{time:0>3} red headquarter stops making warriors")
            else:
                while red[i1][1] > M1:
                    i1 += 1
                    i1 %= 5
                M1 -= red[i1][1]
                list1[i1] += 1
                print(f"{time:0>3} red {red[i1][0]} {time+1} born with strength {red[i1][1]},{list1[i1]} {red[i1][0]} in red headquarter")
                i1 += 1
                i1 %= 5
        if flag2:
            if M2 < minlife:
                flag2 = False
                print(f"{time:0>3} blue headquarter stops making warriors")
            else:
                while blue[i2][1] > M2:
                    i2 += 1
                    i2 %= 5
                M2 -= blue[i2][1]
                list2[i2] += 1
                print(f"{time:0>3} blue {blue[i2][0]} {time+1} born with strength {blue[i2][1]},{list2[i2]} {blue[i2][0]} in blue headquarter")
                i2 += 1
                i2 %= 5
        time += 1