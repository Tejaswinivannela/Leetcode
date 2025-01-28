class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to simplify finding unique quadruplets
        results = []

        def kSum(nums, target, k):
            if not nums:
                return []
            
            # Base case: 2Sum problem
            if k == 2:
                left, right = 0, len(nums) - 1
                pairs = []
                while left < right:
                    current_sum = nums[left] + nums[right]
                    if current_sum == target:
                        pairs.append([nums[left], nums[right]])
                        left += 1
                        right -= 1
                        # Skip duplicates
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
                return pairs

            # Recursive case: reduce kSum to (k-1)Sum
            results = []
            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i - 1]:  # Skip duplicates
                    for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        results.append([nums[i]] + subset)
            return results

        return kSum(nums, target, 4)

        