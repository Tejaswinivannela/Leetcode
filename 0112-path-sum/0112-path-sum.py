class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # Base case: if the root is None, return False
        if not root:
            return False
        
        # If it's a leaf node, check if the remaining targetSum equals the node's value
        if not root.left and not root.right:
            return root.val == targetSum
        
        # Recursively check the left and right subtrees with the updated target sum
        targetSum -= root.val
        return (self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum))
