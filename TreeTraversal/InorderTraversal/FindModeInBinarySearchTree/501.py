"""
LeetCode #501: Find Mode in Binary Search Tree

https://leetcode.com/problems/find-mode-in-binary-search-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root):
        modes = []
        prev = None
        count = 0
        max_count = 0
        
        def dfs(node):
            nonlocal prev, count, max_count
            
            if not node:
                return
            
            # inorder traversal
            dfs(node.left)
            
            # update frequency
            if prev == node.val:
                count += 1
            else:
                count = 1
            
            prev = node.val
            
            # update modes
            if count > max_count:
                max_count = count
                modes.clear()
                modes.append(node.val)
            elif count == max_count:
                modes.append(node.val)
            
            dfs(node.right)
        
        dfs(root)
        return modes