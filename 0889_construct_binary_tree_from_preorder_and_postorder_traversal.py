# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        '''IDEA'''
        # Preorder - root, left, right
        # Postorder - left, right, root

        # [1, 2, 4, 5, 3, 6, 7] pre and [4, 5, 2, 6, 7, 3, 1] post
        # given 1 is root, remove 1 from front of pre and back of post

        # split to calling left, with [2, 4, 5] pre and [4, 5, 2] post
        # --> remove 2, call [4] pre [4] post (left) and [5] pre [5] post (right)

        # and call right with [3, 6, 7] pre and [6, 7, 3] post
        # --> remove 3, call [6] pre [6] post (left) and [7] pre [7] post (right)

        # Function that takes in current node, pre_order and post_order,
        # removes the root of this subtree,
        # determines the pre_order and post_order of its left and right subtree
        # sets value to the current node,
        # and calls dfs(left) and dfs(right),
        # doesn't call left or right if there is only 1 node
        def dfs(node, pre_order, post_order):

            # If the pre_order and post_order have only 1 node, then set the value and return
            if len(pre_order) == 1 and len(post_order) == 1:
                node.val = pre_order[0]
                return

            # Extract root and set value
            root = pre_order[0]
            node.val = root

            # Remove root value from the pre_order and post_order lists
            new_pre_order = pre_order[1:]
            new_post_order = post_order[:-1]

            '''LEFT'''

            # Determine root of left subtree
            left_root = new_pre_order[0]

            # Count the elements in the left sub tree, by adding all elements
            # in post order until element = left_root
            left_elements = 0
            for i in range(len(new_post_order)):
                left_elements += 1
                if new_post_order[i] == left_root:
                    break

            # Determine pre_order and post_order of left subtree using the number of left elements
            left_pre_order = new_pre_order[:left_elements]
            left_post_order = new_post_order[:left_elements]

            # Set left node to a new TreeNode() and recursively call dfs on the left subtree
            node.left = TreeNode()
            dfs(node.left, left_pre_order, left_post_order)

            '''RIGHT'''

            # If there is no right subtree, then skip
            if left_elements == len(new_post_order):
                return
                
            # repeat the same thing for right, use left_elements to determine
            # the contents for the right pre order and right post order
            right_root = new_pre_order[left_elements]

            # Determine pre_order and post_order of right subtree
            right_pre_order = new_pre_order[left_elements:]
            right_post_order = new_post_order[left_elements:]

            # Set right node to a new TreeNode() and recursively call dfs on the right subtree
            node.right = TreeNode()
            dfs(node.right, right_pre_order, right_post_order)


        # Initiate new tree, call dfs
        tree = TreeNode()
        dfs(tree, preorder, postorder)

        return tree