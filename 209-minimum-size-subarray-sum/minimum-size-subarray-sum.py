class Solution(object):
    def minSubArrayLen(self, target, nums):
       
       left = 0
       min_length = float('inf')
       sum1 = 0
       for i in range(0,len(nums)):
        sum1+=nums[i]
        while(sum1>=target):
            min_length = min(min_length,i-left+1)
            sum1-=nums[left]
            left+=1
       return 0 if min_length == float('inf') else  min_length     
