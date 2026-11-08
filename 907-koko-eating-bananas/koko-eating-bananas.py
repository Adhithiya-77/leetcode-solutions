class Solution(object):

  def minEatingSpeed(self, piles, h):
    low = 1
    high = max(piles)
    ans = high
    while low <= high:
      speed = (low + high) // 2
      if self.caneat(piles, h, speed):
        ans = speed
        high = speed - 1 
      else:
        low = speed + 1  
    return ans

  def caneat(self, piles, h, k):
    hours = 0
    for pile in piles:
      hours += (pile + k - 1) // k
    return hours <= h