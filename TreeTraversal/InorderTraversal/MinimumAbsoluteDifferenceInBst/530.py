"""
LeetCode #530: Minimum Absolute Difference in BST

https://leetcode.com/problems/minimum-absolute-difference-in-bst/
"""

class Solution:
    def getMinimumDifference(self, root):
        prev = None
        min_diff = float('inf')
        
        def dfs(node):
            nonlocal prev, min_diff
            if not node:
                return
            
            # inorder traversal
            dfs(node.left)
            
            # compute difference with previous node
            if prev is not None:
                min_diff = min(min_diff, node.val - prev)
            
            prev = node.val
            
            dfs(node.right)
        
        dfs(root)
        return min_diff