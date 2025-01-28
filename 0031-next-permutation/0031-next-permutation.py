class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None, modifies nums in-place
        """
        # Step 1: Find the pivot (first decrease from the right)
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Step 2: If there is a valid pivot, find the number to swap with
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 3: Reverse the suffix
        nums[i + 1:] = reversed(nums[i + 1:])

        