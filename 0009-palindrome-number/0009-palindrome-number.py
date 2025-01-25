class Solution:
    def isPalindrome(self, x):
        # Step 1: Handle negative numbers
        if x < 0:
            return False
        
        # Step 2: Handle numbers that end in 0 but are not 0 themselves (e.g., 10, 100, etc.)
        if x != 0 and x % 10 == 0:
            return False
        
        # Step 3: Reverse the second half of the number
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # Step 4: Check if the first half equals the second half (or with middle digit for odd-length numbers)
        return x == reversed_half or x == reversed_half // 10
