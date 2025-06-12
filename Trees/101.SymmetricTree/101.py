# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def sym(p,q):
            if (not p) and (not q):
                return True
            if not (p and q):
                return False
            if p.val != q.val:
                return False
            if not (sym(p.left,q.right)):
                return False
            if not (sym(p.right,q.left)):
                return False
            return True
        return sym(root.left,root.right)
            

        