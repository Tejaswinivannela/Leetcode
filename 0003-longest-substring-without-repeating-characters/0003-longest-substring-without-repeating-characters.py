
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window approach
        char_set = set()  # To store unique characters in the current window
        left = 0  # Left pointer of the sliding window
        max_length = 0  # To store the maximum length of the substring

        for right in range(len(s)):  # Iterate with the right pointer
            while s[right] in char_set:
                char_set.remove(s[left])  # Remove left character to shrink window
                left += 1  # Move the left pointer
            char_set.add(s[right])  # Add the current character to the set
            max_length = max(max_length, right - left + 1)  # Update max length

        return max_length


# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    s1 = "abcabcbb"
    print("Output for Example 1:", solution.lengthOfLongestSubstring(s1))  # Output: 3

    # Example 2
    s2 = "bbbbb"
    print("Output for Example 2:", solution.lengthOfLongestSubstring(s2))  # Output: 1

    # Example 3
    s3 = "pwwkew"
    print("Output for Example 3:", solution.lengthOfLongestSubstring(s3))  # Output: 3

    # Example 4
    s4 = ""
    print("Output for Example 4:", solution.lengthOfLongestSubstring(s4))  # Output: 0
