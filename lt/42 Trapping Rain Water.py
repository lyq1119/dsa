class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        res = 0
        
        while left < right:
            # 哪边短，就更新哪边。因为水的上限由短板决定（木桶效应）
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    res += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    res += right_max - height[right]
                right -= 1
                
        return res