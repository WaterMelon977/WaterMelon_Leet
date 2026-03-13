"""
LeetCode #226: Invert Binary Tree

https://leetcode.com/problems/invert-binary-tree/
"""


from typing import Optional

class Solution:
    def invertTree(self, root: Optional['TreeNode']) -> Optional['TreeNode']:
        if not root:
            return None
        
        # swap children
        root.left, root.right = root.right, root.left
        
        # recurse on children
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root