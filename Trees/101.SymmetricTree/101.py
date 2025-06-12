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
            

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def isMirror(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and isMirror(p.left, q.right) and isMirror(p.right, q.left)

        return isMirror(root.left, root.right)
    

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def same(root1, root2):
            if not root1 and not root2:
                return True
 
            if not root1 or not root2:
                return False
            
            if root1.val != root2.val:
                return False
            
            return same(root1.left, root2.right) and same(root1.right, root2.left)
 
        return same(root, root)
        # Time: O(n)
        # Space: O(height) or O(n)
