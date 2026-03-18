"""
LeetCode #863: All Nodes Distance K in Binary Tree

https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
"""

class Solution:
    def distanceK(self, root, target, k):
        result = []
        
        # Collect all nodes 'distance' steps below this node
        def collect_downward(node, distance):
            if not node:
                return
            
            if distance == 0:
                result.append(node.val)
                return
            
            collect_downward(node.left, distance - 1)
            collect_downward(node.right, distance - 1)
        
        # Returns distance from current node to target
        # If target not in subtree → return -1
        def dfs_find_distance(current_node):
            if not current_node:
                return -1
            
            # Case 1: Found the target node
            if current_node == target:
                collect_downward(current_node, k)  # explore downward
                return 0  # distance to itself
            
            # Search left and right subtrees
            left_distance = dfs_find_distance(current_node.left)
            right_distance = dfs_find_distance(current_node.right)
            
            # Case 2: Target found in LEFT subtree
            if left_distance != -1:
                distance_from_current = left_distance + 1
                
                # If current node itself is k distance away
                if distance_from_current == k:
                    result.append(current_node.val)
                else:
                    # Explore RIGHT subtree (opposite side)
                    remaining_distance = k - (left_distance + 2)
                    collect_downward(current_node.right, remaining_distance)
                
                return distance_from_current
            
            # Case 3: Target found in RIGHT subtree
            if right_distance != -1:
                distance_from_current = right_distance + 1
                
                if distance_from_current == k:
                    result.append(current_node.val)
                else:
                    # Explore LEFT subtree (opposite side)
                    remaining_distance = k - (right_distance + 2)
                    collect_downward(current_node.left, remaining_distance)
                
                return distance_from_current
            
            # Case 4: Target not found in either subtree
            return -1
        
        dfs_find_distance(root)
        return result