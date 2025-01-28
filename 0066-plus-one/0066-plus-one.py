class Solution:
    def plusOne(self, digits):
        # Start from the last digit and go backwards
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1  # No carry, just increment
                return digits
            digits[i] = 0  # Set current digit to 0 if there's a carry
        
        # If we exit the loop, it means all digits were 9, so we need to add a 1 at the beginning
        return [1] + digits
