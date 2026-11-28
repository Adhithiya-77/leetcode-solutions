class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0

        current  = 0

        for num in nums:
            if num == 1:
                current+=1
                max_len = max(max_len,current)
            else:
                
                current = 0

        return max_len            
        