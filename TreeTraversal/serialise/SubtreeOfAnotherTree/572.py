"""
LeetCode #572: Subtree of Another Tree

https://leetcode.com/problems/subtree-of-another-tree/
"""

class Solution:
    def isSubtree(self, root, subRoot):
        
        def serialize(node):
            if not node:
                return "#"
            
            left = serialize(node.left)
            right = serialize(node.right)
            
            # postorder: left, right, node
            return f"{left},{right},{node.val}"
        
        root_serial = serialize(root)
        sub_serial = serialize(subRoot)
        
        return sub_serial in root_serial