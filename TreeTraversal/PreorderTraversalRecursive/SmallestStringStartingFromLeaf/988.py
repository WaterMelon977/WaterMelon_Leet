"""
LeetCode #988: Smallest String Starting From Leaf

https://leetcode.com/problems/smallest-string-starting-from-leaf/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root):
        self.smallest = None
        
        def dfs(node, path):
            if not node:
                return
            
            # append current character
            path.append(chr(node.val + ord('a')))
            
            # if leaf node
            if not node.left and not node.right:
                candidate = ''.join(reversed(path))
                
                if self.smallest is None or candidate < self.smallest:
                    self.smallest = candidate
            
            # continue traversal
            dfs(node.left, path)
            dfs(node.right, path)
            
            # backtrack
            path.pop()
        
        dfs(root, [])
        return self.smallest