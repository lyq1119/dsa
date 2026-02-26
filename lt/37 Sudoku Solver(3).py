class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        # 使用位运算掩码：1022 代表 1-9 全占用的二进制掩码
        rows, cols, boxes = [0]*9, [0]*9, [0]*9
        vacant = []

        def get_box(r, c): return (r // 3) * 3 + c // 3

        def toggle(r, c, val_int):
            mask = 1 << val_int
            rows[r] ^= mask
            cols[c] ^= mask
            boxes[get_box(r, c)] ^= mask

        # 初始化状态
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    toggle(r, c, int(board[r][c]))
                else:
                    vacant.append((r, c))

        def dfs(k):
            if k == len(vacant): return True
            
            # 这里可以加入简单的 MRV 优化：找当前限制最多的格子
            # 但对于 LeetCode 37，简单的顺序搜索配合位运算已经足够快
            r, c = vacant[k]
            
            # 计算当前格子可填的数字：1 代表可选
            # rows | cols | boxes 得到已占用的，取反得到可选的
            available = ~(rows[r] | cols[c] | boxes[get_box(r, c)]) & 0x3FE
            
            while available:
                # 提取最后一个 1 (Lowbit)
                lowbit = available & -available
                val_int = lowbit.bit_length() - 1 # 获取是第几个数字
                
                board[r][c] = str(val_int)
                toggle(r, c, val_int)
                if dfs(k + 1): return True
                
                # 回溯
                toggle(r, c, val_int)
                board[r][c] = "."
                available &= available - 1 # 去掉已尝试的数字
                
            return False

        dfs(0)