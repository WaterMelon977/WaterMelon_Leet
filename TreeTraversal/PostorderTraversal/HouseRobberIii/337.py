"""
LeetCode #337: House Robber III

https://leetcode.com/problems/house-robber-iii/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return (0, 0)  # (rob_this, skip_this)
            rob_left, skip_left = dfs(node.left)
            rob_right, skip_right = dfs(node.right)

            rob_this = node.val + skip_left + skip_right

            skip_this = max(rob_left, skip_left) + max(rob_right, skip_right)
            return (rob_this, skip_this)

        rob_root, skip_root = dfs(root)
        return max(rob_root, skip_root)
