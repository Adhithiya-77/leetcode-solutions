class Solution(object):
    def moveZeroes(self, nums):
      
       left = 0 
       for i in range(0,len(nums)):
         if nums[i]!=0:
            nums[i],nums[left]=nums[left],nums[i]
            left+=1
       return nums      

        