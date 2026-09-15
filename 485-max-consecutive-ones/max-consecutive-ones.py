class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        current_ones = 0
        max_ones = 0
        for i in range(0,len(nums)):
            if nums[i]==1:
                current_ones+=1
            else:
                max_ones = max(max_ones,current_ones)
                current_ones = 0
        return max(max_ones,current_ones)            
        