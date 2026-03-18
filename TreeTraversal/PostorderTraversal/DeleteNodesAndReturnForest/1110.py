"""
LeetCode #1110: Delete Nodes And Return Forest

https://leetcode.com/problems/delete-nodes-and-return-forest/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        forest = []

        def dfs(node):
            if not node:
                return None

            # Process children first (postorder)
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            # If current node needs to be deleted
            if node.val in to_delete_set:
                # Add children as new roots if they exist
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)
                return None  # delete this node

            return node  # keep this node

        # Start DFS
        root = dfs(root)

        # If root is not deleted, add it
        if root:
            forest.append(root)

        return forest
