class Solution(object):
    def lengthOfLongestSubstring(self, s):
      map = {}
      max_len = 0
      left = 0
      for right in range(len(s)):
        if s[right] in map:
            left = max(left,map[s[right]]+1)
        map[s[right]] = right 

        max_len = max(max_len,right-left+1)   

      return max_len       
