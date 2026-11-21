class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            if len(str(i))%2==0:
                result+=1
        return result        
        