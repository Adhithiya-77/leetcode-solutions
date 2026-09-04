class Solution(object):
    def firstStableIndex(self, nums, k):
        n = len(nums)
        for i in range(0,len(nums)):
            a = max(nums[0:i+1]) - min(nums[i:n])
            if a <=k:
                return i
        return -1         

        