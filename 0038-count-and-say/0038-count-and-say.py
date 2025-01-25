class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case: The first term in the sequence
        if n == 1:
            return "1"
        
        # Recursive case: Generate the (n-1)th term
        prev = self.countAndSay(n - 1)
        
        # Generate the nth term using Run-Length Encoding (RLE)
        result = []
        count = 1
        
        # Iterate through the previous term
        for i in range(1, len(prev)):
            if prev[i] == prev[i - 1]:
                count += 1  # Count consecutive characters
            else:
                # Append the count and the character
                result.append(str(count))
                result.append(prev[i - 1])
                count = 1  # Reset count
        
        # Append the last group
        result.append(str(count))
        result.append(prev[-1])
        
        # Join the result and return as a string
        return ''.join(result)
 