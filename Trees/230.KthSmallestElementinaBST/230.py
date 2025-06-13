# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack=[]
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            stack.append(root.val)
            dfs(root.right)
        
        dfs(root)
        return stack[k-1]

            

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [k]
        ans = [0]
 
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
 
            if count[0] == 1:
                ans[0] = node.val
            
            count[0] = count[0] - 1
            if count[0] > 0:
                dfs(node.right)
        
        dfs(root)
        return ans[0]

            

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack=[]
        while True:
            while root:
                stack.append(root)
                root=root.left
            root = stack.pop()
            k-=1
            if k==0:
                return root.val
            root=root.right
