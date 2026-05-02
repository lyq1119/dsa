# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def construct(node):
            if not node:
                return ""
            mystr = f"{node.val}"
            if node.left and node.right:
                mystr += f" ( {construct(node.left)} , {construct(node.right)} )"
            elif node.left:
                mystr += f" ( {construct(node.left)} , )"
            elif node.right:
                mystr += f" ( , {construct(node.right)} )"
            return mystr
        return construct(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        mylist = data.split()
        stack = [TreeNode(int(mylist[0]))]
        for i in range(1,len(mylist)):
            obj = mylist[i]
            if obj == "(" or obj == ",":
                stack.append(obj)
            elif obj == ")":
                flagr = True
                rightnode = None
                leftnode = None
                while stack and stack[-1] != "(":
                    t = stack.pop()
                    if t == ',':
                        flagr = False
                        continue
                    if flagr:
                        rightnode = t
                    else:
                        leftnode = t
                stack.pop()
                stack[-1].left = leftnode
                stack[-1].right = rightnode
            else:
                stack.append(TreeNode(int(obj)))
        return stack[0]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

code = Codec()
print(code.deserialize(code.serialize(root)).left)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))