class Solution(object):
    def maxProduct(self, nums):
       prefix = 1
       suffix = 1
       ans = float('-inf')
       n = len(nums)
       for i in range(0,len(nums)):
        if suffix ==0:
            suffix = 1
        if prefix ==0:
            prefix = 1
        prefix*=nums[i]
        suffix*=nums[n-1-i]
        ans = max(ans,suffix,prefix)
       return ans         