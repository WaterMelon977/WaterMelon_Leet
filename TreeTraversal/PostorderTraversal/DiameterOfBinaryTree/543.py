"""
LeetCode #543: Diameter of Binary Tree

https://leetcode.com/problems/diameter-of-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def dfs(node):
            self.diameter
            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # update self.diameter
            self.diameter = max(self.diameter, left_height + right_height)
            
            # return height
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.diameter