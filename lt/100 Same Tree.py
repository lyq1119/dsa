class Solution:
    def isSameTree(self, p, q) -> bool:
        def check(p,q):
            if not p and not q:
                return True
            if p and q:
                if p.val != q.val:
                    return False
                return check(p.left,q.left) and check(p.right,q.right)
            return False
        return check(p,q)