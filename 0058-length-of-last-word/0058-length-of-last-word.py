class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Strip leading and trailing spaces, then split by spaces
        words = s.strip().split()
        # Return the length of the last word
        return len(words[-1])
