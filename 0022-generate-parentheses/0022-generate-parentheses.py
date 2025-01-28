class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        # Helper function to generate combinations using backtracking
        def backtrack(current, open_count, close_count):
            # If the current string has reached the maximum length
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add an open parenthesis if there are open parentheses left to add
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Add a close parenthesis if it won't create an invalid sequence
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        # Start the backtracking with an empty string and no parentheses added
        backtrack("", 0, 0)
        return result

        