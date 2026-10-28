class Solution(object):
    def nextGreaterElements(self, nums):
       n = len(nums)
       ans = [-1] *n
       stack = []

       for i in range(2*n-1,-1,-1):
        num = nums[i%n]

        while stack and stack[-1] <= num:
            stack.pop()

        if i<n and stack:
            ans[i] = stack[-1]
        stack.append(num)
       return ans          