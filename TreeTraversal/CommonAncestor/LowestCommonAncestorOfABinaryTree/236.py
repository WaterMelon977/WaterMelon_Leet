"""
LeetCode #236: Lowest Common Ancestor of a Binary Tree

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def dfs(node):
            if not node:
                return None
            
            # If current node is p or q
            if node == p or node == q:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If both sides found → this is LCA
            if left and right:
                return node
            
            # Otherwise return whichever side found something
            return left if left else right
        
        return dfs(root)