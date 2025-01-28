class Solution:
    def addBinary(self, a, b):
        # Initialize pointers for both strings and a carry variable
        i, j, carry = len(a) - 1, len(b) - 1, 0
        result = []
        
        # Traverse both strings from the end to the beginning
        while i >= 0 or j >= 0 or carry:
            # Get the current digits (if any) or 0 if the string is exhausted
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0
            
            # Add the bits and the carry
            total = bit_a + bit_b + carry
            
            # The result's current digit will be the remainder of total divided by 2
            result.append(str(total % 2))
            
            # Update the carry (total // 2 will be either 0 or 1)
            carry = total // 2
            
            # Move to the next digits
            i -= 1
            j -= 1
        
        # Since we built the result backwards, reverse it before joining
        return ''.join(reversed(result))
