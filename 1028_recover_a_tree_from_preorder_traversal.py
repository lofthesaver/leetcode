# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:

        # Extract dictionary of depths, and node values
        dash_count = 0
        node_values = []
        node_depths = []

        i = 0
        while i < len(traversal):

            # If the character not a dash, then add to node value,
            # if character is dash then increment count of dashes
            if traversal[i] != "-":

                curr_c = ""
                while i < len(traversal) and traversal[i] != "-":
                    curr_c += traversal[i]
                    i += 1

                node_values.append(int(curr_c))
                node_depths.append(dash_count)
                dash_count = 0

            else:
                dash_count += 1
                i += 1

        # keep track of the current node value using index
        curr_node_index = [0]

        # Create new tree node to recover
        node = TreeNode()

        # DFS
        def dfs(node):

            # If out of range, return
            if curr_node_index[0] >= len(node_values):
                return

            # Get current value and current depth
            curr_value = node_values[curr_node_index[0]]
            curr_depth = node_depths[curr_node_index[0]]

            # Set node value using current node index
            node.val = node_values[curr_node_index[0]]

            # If this is the last number, return
            if curr_node_index[0] == len(node_values) - 1:
                return

            # If left depth greater than curr depth, increment curr node index and dfs left
            if node_depths[curr_node_index[0] + 1] > curr_depth:
                curr_node_index[0] += 1

                # Set node.left to not null, dfs
                node.left = TreeNode()
                dfs(node.left)

            # If this is the last number, return
            if curr_node_index[0] == len(node_values) - 1:
                return

            # If right depth greater than curr depth, increment curr node index and dfs right
            if node_depths[curr_node_index[0] + 1] > curr_depth:
                curr_node_index[0] += 1

                # Set node.right to not null, dfs
                node.right = TreeNode()
                dfs(node.right)

        # Call dfs on the new node and return
        dfs(node)
        return node