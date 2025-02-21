# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right'


class FindElements:

    def __init__(self, root: Optional[TreeNode]):

        # Keep track of current values
        self.values = {0}

        # Initialize root.val to 0
        root.val = 0
        
        def dfs(root):
            # Go left
            if root.left != None:

                # Set left value
                root.left.val = 2 * root.val + 1
                
                # Add the value to self.values
                self.values.add(root.left.val)
                dfs(root.left)
                
            # Go right
            if root.right != None:

                # Set right value
                root.right.val = 2 * root.val + 2

                # Add value to self.values
                self.values.add(root.right.val)
                dfs(root.right)

        # Call dfs on root
        dfs(root)

    def find(self, target: int) -> bool:
        return target in self.values
        

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)