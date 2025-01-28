class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Stack to keep track of opening brackets
        stack = []
        # Hash map for mapping closing to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map:
                # Check the top of the stack or use a dummy value if stack is empty
                top_element = stack.pop() if stack else '#'
                # If the top of the stack doesn't match the current closing bracket, return False
                if bracket_map[char] != top_element:
                    return False
            else:
                # Push opening brackets onto the stack
                stack.append(char)

        # If the stack is empty, all brackets are valid and properly closed
        return not stack
