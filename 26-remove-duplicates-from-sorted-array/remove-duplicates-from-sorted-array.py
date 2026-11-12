class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        

        if not nums:
            return 0

        # Pointer for the position of the next unique element
        k = 1  

        # Start from second element and compare with previous
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k

        