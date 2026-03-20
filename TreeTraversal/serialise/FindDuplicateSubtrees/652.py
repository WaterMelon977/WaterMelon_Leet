"""
LeetCode #652: Find Duplicate Subtrees

https://leetcode.com/problems/find-duplicate-subtrees/
"""


class Solution:
    def findDuplicateSubtrees(self, root):
        from collections import defaultdict
        
        count = defaultdict(int)
        result = []
        
        def dfs(node):
            if not node:
                return "#"  # marker for null
            
            left_serial = dfs(node.left)
            right_serial = dfs(node.right)
            
            # Serialize current subtree
            serial = f"{node.val},{left_serial},{right_serial}"
            
            count[serial] += 1
            
            # Add only when seen second time
            if count[serial] == 2:
                result.append(node)
            
            return serial
        
        dfs(root)
        return result