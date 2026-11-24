class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {} # Stores character -> last seen index
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # If the character is already in the map and within the current window
            if s[right] in char_map and char_map[s[right]] >= left:
                # Move left pointer to skip the duplicate
                left = char_map[s[right]] + 1
            
            # Update the last seen index of the character
            char_map[s[right]] = right
            
            # Calculate window size and update max_length
            max_length = max(max_length, right - left + 1)
            
        return max_length