class Solution:
    def myAtoi(self, s):
        # Define the 32-bit integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Step 1: Trim leading whitespace
        s = s.lstrip()
        if not s:
            return 0  # If string is empty after trimming

        # Step 2: Handle optional sign
        sign = 1  # Assume positive
        i = 0  # Pointer to traverse the string
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        # Step 3: Read digits
        result = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])

            # Check for overflow/underflow
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        # Step 4: Apply sign and return the result
        return sign * result
