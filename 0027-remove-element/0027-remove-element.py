class Solution:
    def removeElement(self, nums, val):
        k = 0  # Pointer for the position of the next valid element.
        
        for i in range(len(nums)):
            if nums[i] != val:  # If the current element is not equal to val:
                nums[k] = nums[i]  # Move it to the position pointed by k.
                k += 1  # Increment k to point to the next available position.
        
        # After the loop, k is the count of elements not equal to val.
        return k
