class Solution(object):
    def pivotIndex(self, nums):
        n = len(nums)
        for i in range(0,len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:n]):
                return i
        return -1        