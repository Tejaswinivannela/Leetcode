class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int):
        result = []
        
        def dfs(node, current_path, remaining_sum):
            # Base case: if the node is None, return
            if not node:
                return
            
            # Add the current node's value to the path
            current_path.append(node.val)
            
            # If it's a leaf node and the remaining sum is 0, add the path to result
            if not node.left and not node.right and remaining_sum == node.val:
                result.append(list(current_path))
            
            # Recurse on left and right children with updated remaining sum
            dfs(node.left, current_path, remaining_sum - node.val)
            dfs(node.right, current_path, remaining_sum - node.val)
            
            # Backtrack: remove the current node from the path before returning
            current_path.pop()
        
        # Start DFS from the root
        dfs(root, [], targetSum)
        
        return result
