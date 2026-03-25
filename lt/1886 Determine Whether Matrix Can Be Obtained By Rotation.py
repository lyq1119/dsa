class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        flag = True
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[-i-1][-j-1]:
                    flag = False
        if flag:
            return True
        flag = True
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[j][-i-1]:
                    flag = False
        if flag:
            return True
        flag = True
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[-j-1][i]:
                    flag = False
        if flag:
            return True
        flag = True
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[i][j]:
                    flag = False
        if flag:
            return True
        return False