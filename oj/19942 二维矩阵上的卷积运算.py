class Matrix():
    def __init__(self, row, col, val):
        self.row = row
        self.col = col
        self.val = val

    def __add__(self, other):
        if self.row != other.row or self.col != other.col:
            raise ValueError
        ans = [[self.val[i][j] + other.val[i][j] for j in range(self.col)] for i in range(self.row)]
        return Matrix(self.row, self.col, ans)

    def __str__(self):
        ans = []
        for r in self.val:
            ans.append(" ".join(map(str, r)))
        return "\n".join(ans)

    def __mul__(self, other):
        if self.col != other.row:
            raise ValueError
        ans = [[0 for i in range(other.col)] for j in range(self.row)]
        for i in range(self.row):
            for j in range(other.col):
                for k in range(self.col):
                    ans[i][j] += self.val[i][k] * other.val[k][j]
        return Matrix(self.row, other.col, ans)

class ConvMatrix(Matrix):
    def __init__(self, row, col, val):
        super().__init__(row, col, val)

    def conv2d(self, kernel):
        # 获取卷积核的尺寸
        k_row, k_col = len(kernel), len(kernel[0])

        # 计算输出矩阵的尺寸
        out_row = self.row - k_row + 1
        out_col = self.col - k_col + 1

        # 初始化输出矩阵
        output_val = [[0] * out_col for _ in range(out_row)]

        # 进行卷积运算
        for i in range(out_row):
            for j in range(out_col):
                for ki in range(k_row):
                    for kj in range(k_col):
                        output_val[i][j] += self.val[i + ki][j + kj] * kernel[ki][kj]

        return Matrix(out_row, out_col, output_val)


if __name__ == "__main__":
    m, n, p, q = map(int, input().split())
    M = ConvMatrix(m, n, [list(map(int, input().split())) for _ in range(m)])

    kernel = []
    for _ in range(p):
        kernel.append(list(map(int, input().split())))

    result = M.conv2d(kernel)
    for row in result.val:
        print(" ".join(map(str, row)))