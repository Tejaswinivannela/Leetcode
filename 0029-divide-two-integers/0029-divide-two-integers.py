class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Define the boundary for 32-bit signed integers
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle edge case where dividend is the smallest 32-bit integer
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine the sign of the result
        sign = -1 if (dividend < 0) != (divisor < 0) else 1
        
        # Work with positive numbers for simplicity
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        # Subtract divisor powers of two times from the dividend
        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1
            # Double the divisor until it's larger than the dividend
            while dividend >= temp_divisor << 1:
                temp_divisor <<= 1
                multiple <<= 1
            # Subtract the found largest multiple of divisor
            dividend -= temp_divisor
            quotient += multiple
        
        # Apply the sign to the result
        return sign * quotient
