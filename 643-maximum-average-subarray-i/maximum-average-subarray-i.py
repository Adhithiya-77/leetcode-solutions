class Solution(object):
    def findMaxAverage(self, nums, k):

        prefix_sum = 0
        for i in range(0,k):
            prefix_sum+=nums[i]
        
        max_sum = prefix_sum

        for j in range(k,len(nums)):
            prefix_sum -= nums[j-k]

            prefix_sum+= nums[j]

            max_sum = max(prefix_sum,max_sum)

        return float(max_sum)/k    
       
        