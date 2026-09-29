class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n
        

        
        for i in range(1,n):
            ans[i] = ans[i-1] * nums[i-1]

        right = 1

        for j in range(n-1,-1,-1):
            ans[j]*= right
            right *= nums[j]

        return ans        
