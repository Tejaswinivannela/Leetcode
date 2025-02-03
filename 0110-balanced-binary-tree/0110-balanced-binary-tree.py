class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
    
        def height(node):
            if not node:  # If node is None, its height is 0
                return 0
            
            left_height = height(node.left)  # Get the height of the left subtree
            if left_height == -1:  # Left subtree is unbalanced
                return -1
            
            right_height = height(node.right)  # Get the height of the right subtree
            if right_height == -1:  # Right subtree is unbalanced
                return -1
            
            # If the current node is unbalanced
            if abs(left_height - right_height) > 1:
                return -1
            
            # Return the height of the current node
            return 1 + max(left_height, right_height)
        
        # If the tree is balanced, the root height will not be -1
        return height(root) != -1
