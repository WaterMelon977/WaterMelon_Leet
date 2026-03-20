"""
LeetCode #2458: Height of Binary Tree After Subtree Removal Queries

https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/
"""

class Solution:
    def treeQueries(self, root, queries):
        subtree_height = {}
        
        # Step 1: compute subtree heights
        def get_height(node):
            if not node:
                return -1  # so leaf = 0
            left = get_height(node.left)
            right = get_height(node.right)
            h = 1 + max(left, right)
            subtree_height[node.val] = h
            return h
        
        get_height(root)

        res = {}
        
        # Step 2: reroot DFS to compute "up" values
        def dfs(node, depth, up_val):
            if not node:
                return
            
            res[node.val] = up_val
            
            # Heights of children
            left_h = subtree_height.get(node.left.val, -1) if node.left else -1
            right_h = subtree_height.get(node.right.val, -1) if node.right else -1
            
            # For left child
            if node.left:
                new_up_left = max(
                    up_val,                          # from ancestors
                    depth + 1 + right_h             # via sibling
                )
                dfs(node.left, depth + 1, new_up_left)
            
            # For right child
            if node.right:
                new_up_right = max(
                    up_val,
                    depth + 1 + left_h
                )
                dfs(node.right, depth + 1, new_up_right)
        
        dfs(root, 0, 0)
        
        return [res[q] for q in queries]