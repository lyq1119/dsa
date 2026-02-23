class Solution:
    def sortedArrayToBST(self, nums):
        def construct(i,j):
            if i > j:
                return None
            mid = (i+j)//2
            a = nums[mid]
            node = TreeNode(a)
            node.left = construct(i,mid-1)
            node.right = construct(mid+1,j)
            return node
        return construct(0,len(nums)-1)
        
