# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lcaDeepestLeaves(self, root):
        
        # DFS returns maximum depth of left and right subtree,
        # and the node
        def dfs(root):

            # If root is None
            if root == None:
                return 0, None

            left_depth, left_node = dfs(root.left)
            right_depth, right_node = dfs(root.right)

            # If left has a greater depth then it means LCA is the left node
            if left_depth > right_depth:
                return left_depth + 1, left_node

            # Else if right has a greater depth then LCA is right node
            elif left_depth < right_depth:
                return right_depth + 1, right_node

            # If the two depths are equal then LCA is the current node
            else:
                return left_depth + 1, root

        depth, node = dfs(root)
        return node