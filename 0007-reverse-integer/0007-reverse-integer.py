class Solution:
    def reverse(self, x):
        # Define the 32-bit integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Determine the sign of the number
        sign = -1 if x < 0 else 1
        x = abs(x)  # Work with the absolute value

        # Reverse the digits
        reversed_x = 0
        while x != 0:
            digit = x % 10  # Get the last digit
            x //= 10  # Remove the last digit from x

            # Check for overflow before adding the digit
            if (reversed_x > INT_MAX // 10) or (reversed_x == INT_MAX // 10 and digit > 7):
                return 0  # Overflow case
            if (reversed_x < INT_MIN // 10) or (reversed_x == INT_MIN // 10 and digit > 8):
                return 0  # Underflow case

            reversed_x = reversed_x * 10 + digit

        return sign * reversed_x  # Restore the sign before returning
