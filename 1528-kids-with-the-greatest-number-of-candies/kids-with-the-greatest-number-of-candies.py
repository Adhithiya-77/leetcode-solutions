class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        a = max(candies)
        for i in candies:
            result.append((i+extraCandies)>=a)
        return result    

        