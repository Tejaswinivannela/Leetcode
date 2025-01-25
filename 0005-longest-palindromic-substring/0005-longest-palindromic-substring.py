class Solution:
    def longestPalindrome(self, s):
        def expand_around_center(left, right):
            # Expand as long as the characters are equal and within bounds
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindromic substring
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # Odd-length palindrome (single character center)
            odd_palindrome = expand_around_center(i, i)
            # Even-length palindrome (two character center)
            even_palindrome = expand_around_center(i, i + 1)
            
            # Update the longest palindrome if needed
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            if len(even_palindrome) > len(longest):
                longest = even_palindrome

        return longest
