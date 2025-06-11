# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced=[True]

        def height(root):
            if not root:
                return 0
            
            left=height(root.left)
            if not balanced[0]:
                return 0

            right=height(root.right)

            if abs(left-right) >1:
                balanced[0]=False
                return 0

            return 1+max(left,right)
        
        height(root)

        return balanced[0]



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            left = height(root.left)
            if left == -1:
                return -1
            right = height(root.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return height(root) != -1



        
        