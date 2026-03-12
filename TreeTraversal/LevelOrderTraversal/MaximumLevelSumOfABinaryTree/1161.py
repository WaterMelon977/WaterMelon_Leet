"""
LeetCode #1161: Maximum Level Sum of a Binary Tree

https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        row_level=0
        maxRowTotal= float('-inf')
        maxRow =0 

        while queue:
            row_size = len(queue)
            row_level +=1 
            row_total=0

            for _ in range(row_size):
                node = queue.popleft()
                row_total += node.val


                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if row_total > maxRowTotal:
                maxRowTotal = row_total
                maxRow = row_level
        return maxRow
                



    
        