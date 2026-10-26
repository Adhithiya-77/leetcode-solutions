class Solution(object):
    def lengthOfLongestSubstring(self, s):
      map = {}
      max_len = 0
      left = 0
      for right in range(len(s)):
        map[s[right]] = map.get(s[right],0)+1

        while map[s[right]] >1:
            map[s[left]] -=1
            left+=1
        max_len = max(max_len,right-left+1)
      return max_len       
