class Solution:
    def isMatch(self, s, p):
        # Initialize a DP table with dimensions (len(s)+1) x (len(p)+1)
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Base case: empty string and empty pattern match
        dp[0][0] = True
        
        # Handle patterns like "a*", "a*b*", etc. that can match an empty string
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # Check if we ignore the '*' or if we match one or more of the preceding character
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] if p[j - 2] == s[i - 1] or p[j - 2] == '.' else False)
        
        # The answer will be in dp[len(s)][len(p)]
        return dp[len(s)][len(p)]
