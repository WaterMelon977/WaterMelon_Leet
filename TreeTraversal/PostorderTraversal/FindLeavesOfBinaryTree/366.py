"""
LeetCode #366: Find Leaves of Binary Tree

https://leetcode.com/problems/find-leaves-of-binary-tree/

plaintext

You are given the root of a binary tree. Your task is to collect the nodes of the tree in a specific way that simulates repeatedly removing leaf nodes.

The process works as follows:

First, identify and collect all current leaf nodes (nodes with no children) into a group
Remove these leaf nodes from the tree
After removal, some nodes that previously had children may now become new leaf nodes
Repeat steps 1-2, collecting each new set of leaf nodes into separate groups
Continue this process until the entire tree is empty
The result should be a list of lists, where each inner list contains the values of nodes that were removed together in the same iteration.

For example, if you have a tree like:

      1
     / \
    2   3
   / \
  4   5
The collection process would be:

First iteration: Collect leaves [4, 5, 3] and remove them
Second iteration: Now 2 is a leaf, collect [2] and remove it
Third iteration: Now 1 is a leaf, collect [1] and remove it
The final output would be: [[4, 5, 3], [2], [1]]

"""



class Solution:
    def findLeaves(self, root):
        res = []
        
        def dfs(node):
            if not node:
                return -1  # base for height calculation
            
            left_h = dfs(node.left)
            right_h = dfs(node.right)
            
            curr_h = 1 + max(left_h, right_h)
            
            # ensure list exists
            if curr_h == len(res):
                res.append([])
            
            res[curr_h].append(node.val)
            
            return curr_h
        
        dfs(root)
        return res
