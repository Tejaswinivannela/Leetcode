class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        
        # Helper function to perform backtracking
        def backtrack(start, target, current_combination):
            # If the target is 0, we've found a valid combination
            if target == 0:
                result.append(list(current_combination))
                return
            # If the target becomes negative, we've exceeded the sum
            if target < 0:
                return
            
            # Try every candidate starting from the current index
            for i in range(start, len(candidates)):
                current_combination.append(candidates[i])
                # Continue the search with reduced target and the same candidate index
                backtrack(i, target - candidates[i], current_combination)
                current_combination.pop()  # Backtrack
        
        # Start backtracking from the first index
        backtrack(0, target, [])
        return result
