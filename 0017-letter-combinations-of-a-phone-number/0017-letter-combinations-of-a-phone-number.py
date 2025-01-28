class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        # Mapping of digits to corresponding letters
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result = []

        def backtrack(index, path):
            # If the current path's length matches the input length, add to result
            if index == len(digits):
                result.append(''.join(path))
                return

            # Get the possible letters for the current digit
            possible_letters = digit_to_letters[digits[index]]
            for letter in possible_letters:
                # Add the letter to the current path
                path.append(letter)
                # Move to the next digit
                backtrack(index + 1, path)
                # Backtrack by removing the last added letter
                path.pop()

        # Start backtracking
        backtrack(0, [])
        return result
