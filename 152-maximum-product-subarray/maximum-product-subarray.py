class Solution(object):
    def maxProduct(self, nums):
      prefix = 1
      suffix = 1
      n = len(nums)
      max_val = float('-inf')
      for i in range(0,len(nums)):
        if suffix == 0:
            suffix = 1
        if prefix == 0:
            prefix = 1
        suffix *= nums[n-i-1]
        prefix *= nums[i]
        max_val = max(max_val,prefix,suffix)
      return max_val  
