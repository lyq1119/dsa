class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # 特判：如果 n 是 0，它的二进制是 "0"，翻转后是 "1"
        if n == 0:
            return 1
        
        mask = 1
        # 构造一个与 n 长度相同的全 1 掩码
        # 例如 n = 5 (101), 最终 mask 会变成 7 (111)
        while mask < n:
            mask = (mask << 1) | 1
            
        # 使用异或运算翻转每一位
        return n ^ mask