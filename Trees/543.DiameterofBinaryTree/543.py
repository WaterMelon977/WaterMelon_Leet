class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        largest_diameter = [0]
 
        def height(root):
            if root is None:
                return 0
 
            left_height = height(root.left)
            right_height = height(root.right)
            diameter = left_height + right_height
 
            largest_diameter[0] = max(largest_diameter[0], diameter)
            
            return 1 + max(left_height, right_height)
 
        height(root)
        return largest_diameter[0]


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def depth(node):
            if not node:
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            self.diameter = max(self.diameter, left_depth + right_depth)
            return 1 + max(left_depth, right_depth)

        depth(root)
        return self.diameter

