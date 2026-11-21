class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0

        for i in nums:
            digit = 0
            while i > 0:
                i //=10
                digit +=1
            if digit % 2 == 0:
                result += 1
        return result              

        