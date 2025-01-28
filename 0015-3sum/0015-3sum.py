class Solution:
    def threeSum(self, nums):
        # Sort the array to enable the two-pointer approach
        nums.sort()
        result = []

        # Iterate through the array
        for i in range(len(nums) - 2):
            # Skip duplicate elements for the first element of the triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two-pointer approach
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # Move pointers and skip duplicates
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
