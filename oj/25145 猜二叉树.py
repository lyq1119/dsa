import sys
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(inorder, postorder):
    """
    递归根据中序和后序序列构建二叉树
    """
    if not inorder or not postorder:
        return None
    
    # 1. 后序遍历的最后一个元素是根节点
    root_val = postorder[-1]
    root = TreeNode(root_val)
    
    # 2. 在中序遍历中找到根节点的位置
    # 题目保证结点不重复，可以直接用 index
    mid_index = inorder.index(root_val)
    
    # 3. 切分中序序列
    left_in = inorder[:mid_index]
    right_in = inorder[mid_index+1:]
    
    # 4. 切分后序序列
    # 左子树在后序中的长度 = 左子树在中序中的长度
    left_len = len(left_in)
    left_post = postorder[:left_len]
    right_post = postorder[left_len:-1] # -1 是为了排除掉已经被消费的根节点
    
    # 5. 递归构建
    root.left = build_tree(left_in, left_post)
    root.right = build_tree(right_in, right_post)
    
    return root

def level_order(root):
    """
    使用队列进行层序遍历 (BFS)
    """
    if not root:
        return ""
    
    queue = deque([root])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
    return "".join(result)

def solve():
    # 读取所有输入
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator)) # 读取组数
        for _ in range(n):
            in_str = next(iterator)   # 中序
            post_str = next(iterator) # 后序
            
            # 建树
            tree_root = build_tree(in_str, post_str)
            # 输出层序
            print(level_order(tree_root))
            
    except StopIteration:
        pass

if __name__ == "__main__":
    solve()