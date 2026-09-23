class Solution(object):
    def maxSubArray(self, nums):
       max_sum = nums[0]
       prefix_sum = 0
       for num in nums:
        prefix_sum+=num
        max_sum = max(max_sum,prefix_sum)
        if prefix_sum<0:
            prefix_sum = 0
       return max_sum     