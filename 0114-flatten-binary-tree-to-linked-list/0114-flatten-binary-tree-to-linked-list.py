class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        # Helper function to flatten the tree
        def flatten_tree(node):
            if not node:
                return None

            # Flatten the left subtree
            left_tail = flatten_tree(node.left)
            
            # Flatten the right subtree
            right_tail = flatten_tree(node.right)
            
            # If there was a left subtree, we move it to the right
            if left_tail:
                # Connect the left tail's right to the right child
                left_tail.right = node.right
                # Move the left subtree to the right
                node.right = node.left
                node.left = None  # Set the left child to None
            
            # Return the "tail" of the flattened subtree
            return right_tail if right_tail else left_tail or node
        
        # Call the helper function to start flattening the tree
        flatten_tree(root)
