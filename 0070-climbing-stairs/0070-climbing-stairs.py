class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        # Initialize base cases
        prev1, prev2 = 1, 2
        
        # Compute the number of ways to reach each step starting from 3 to n
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev1, prev2 = prev2, current
        
        return prev2