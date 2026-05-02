class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        # 先对str2进行kmp
        m = len(str2)
        next = [0 for _ in range(m+1)]
        j = 1
        for i in range(1,m):
            while j != 0 and str2[i] != str2[j-1]:
                j = next[j-1]
            next[i+1] = j
            j += 1
        hao = [False for _ in range(m)]
        hao[0] = True
        cur = m
        while next[cur] != 0:
            hao[m-next[cur]] = True
            cur = next[cur]
        # 先处理所有T的位置
        begin = []
        curlist = ["" for _ in range(len(str1)+len(str2)-1)]
        for i in range(len(str1)):
            if str1[i] == "T":
                if curlist[i] == "":
                    begin.append(i)
                    for j in range(i,i+m):
                        curlist[j] = str2[j-i]
                else:
                    if not hao[i-begin[-1]]:
                        return ""
                    else:
                        for j in range(i,i+m):
                            curlist[j] = str2[j-i]
                        begin[-1] = i
        undetermined = {i for i in range(len(curlist)) if curlist[i] == ""}
        # 检查F
        for i in range(len(str1)):
            if str1[i] == "F":
                flag = False
                for j in range(i,i+m):
                    if curlist[j] == "":
                        flag = True
                        break
                    if curlist[j] != str2[j-i]:
                        flag = True
                        break
                if not flag:
                    return ""
        if not undetermined:
            return "".join(curlist)
        mylist= []
        # 递归构造
        def backtrack(curlist,i):
            nonlocal mylist
            if i >= len(curlist):
                mylist = curlist.copy()
                return True
            # 检查已经确定的位置
            if i not in undetermined:
                if i < m-1:
                    return backtrack(curlist,i+1)
                if str1[i-m+1] == "T":
                    return backtrack(curlist,i+1)
                else:
                    flag = False
                    for j in range(i-m+1,i+1):
                        if curlist[j] != str2[j-i+m-1]:
                            flag = True
                            break
                    if not flag:
                        return False
                    return backtrack(curlist,i+1)
            for letter in letters:
                curlist[i] = letter
                if i < m-1:
                    verdict = backtrack(curlist,i+1)
                    if verdict:
                        return True
                    continue
                flag = False
                for j in range(i-m+1,i+1):
                    if curlist[j] != str2[j-i+m-1]:
                        flag = True
                        break
                if not flag:
                    continue
                verdict = backtrack(curlist,i+1)
                if verdict:
                    return True
            return False
        backtrack(curlist,0)
        return "".join(mylist)
print(Solution().generateString("FFTFFF","a"))