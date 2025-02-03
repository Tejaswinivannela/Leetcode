from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        # Initialize the queue for BFS, starting with the root node at depth 1
        queue = deque([(root, 1)])  # Each element in the queue is a tuple (node, depth)
        
        while queue:
            node, depth = queue.popleft()  # Dequeue the front element
            
            # Check if the current node is a leaf node
            if not node.left and not node.right:
                return depth
            
            # If left child exists, add it to the queue
            if node.left:
                queue.append((node.left, depth + 1))
            
            # If right child exists, add it to the queue
            if node.right:
                queue.append((node.right, depth + 1))
