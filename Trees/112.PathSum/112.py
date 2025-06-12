# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        sett= set()
        
        def getSum(root,total):    
            if not root:
                return
            total += root.val
            if not (root.left or  root.right):
                sett.add(total)
            getSum(root.left ,total)
            getSum(root.right ,total)
        
        
        getSum(root,0)

        return targetSum in sett
            
            
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        sett= set()
        
        def getSum(root,total):    
            if not root:
                return False
            total += root.val
            if not (root.left or  root.right):
                return total == targetSum
            if getSum(root.left ,total):
                return True
            if getSum(root.right ,total):
                return True
            return False        
        
        return getSum(root,0)        
    

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def getSum(root,total):    
            if not root:
                return False
            total += root.val
            
            if not (root.left or  root.right):
                return total == targetSum

            return getSum(root.left, total) or getSum(root.right, total)     
        
        return getSum(root,0)
