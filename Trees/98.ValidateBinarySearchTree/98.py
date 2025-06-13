# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev=[None]

        def dfs(root):
            if not root:
                return True
            
            if not dfs(root.left):
                return False
            
            if prev[0] is not None:
                if root.val <= prev[0]:
                    return False 
            prev[0]=root.val
            
            if not dfs(root.right):
                return False

            return True
        return dfs(root)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node, minn, maxx):
            if not node:
                return True
            
            if node.val <= minn or node.val >= maxx:
                return False
            
            return is_valid(node.left, minn, node.val) and is_valid(node.right, node.val, maxx)
 
        return is_valid(root, float("-inf"), float("inf"))
