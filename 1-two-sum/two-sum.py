class Solution:
   def twoSum(self,nums, target):
      seen = {}

      for i in range(0,len(nums)):

        complement = target - nums[i]

        if complement in seen:
            return[seen[complement],i]
        seen[nums[i]] = i    



        