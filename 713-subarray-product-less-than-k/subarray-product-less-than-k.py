class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
       if k<=1:
        return 0
       count = 0
       left = 0
       prod = 1
       for i in range(0,len(nums)):
        prod*=nums[i]
        while prod>=k:
            prod/= nums[left]
            left +=1
        count+=(i-left+1)
       return count     
