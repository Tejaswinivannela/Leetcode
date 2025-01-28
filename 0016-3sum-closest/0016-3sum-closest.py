class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Sort the array to use two-pointer technique
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')  # Initialize closest sum to infinity

        for i in range(n - 2):
            # Two-pointer approach
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # Update closest_sum if the current_sum is closer to target
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum

                # Move pointers based on comparison with the target
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    # If the sum is exactly equal to target, return it
                    return current_sum

        return closest_sum

        