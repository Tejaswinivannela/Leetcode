class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid  # Target found
            elif nums[mid] < target:
                left = mid + 1  # Narrow down to the right half
            else:
                right = mid - 1  # Narrow down to the left half
        
        # If target is not found, `left` is the insertion position
        return left

        