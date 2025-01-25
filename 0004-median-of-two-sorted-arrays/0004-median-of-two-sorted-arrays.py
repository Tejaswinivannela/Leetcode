class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            # Edge cases: left and right elements around the partitions
            maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minX = float('inf') if partitionX == x else nums1[partitionX]
            maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minY = float('inf') if partitionY == y else nums2[partitionY]

            # Check if we found the correct partition
            if maxX <= minY and maxY <= minX:
                # Handle odd and even cases
                if (x + y) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
                else:
                    return max(maxX, maxY)
            elif maxX > minY:
                high = partitionX - 1  # Move partitionX to the left
            else:
                low = partitionX + 1  # Move partitionX to the right

        raise ValueError("Input arrays are not sorted.")  # Just in case the inputs are invalid

# Example usage
solution = Solution()

# Example 1
nums1 = [1, 3]
nums2 = [2]
print("Output for Example 1:", solution.findMedianSortedArrays(nums1, nums2))  # Output: 2.0

# Example 2
nums1 = [1, 2]
nums2 = [3, 4]
print("Output for Example 2:", solution.findMedianSortedArrays(nums1, nums2)) 
        