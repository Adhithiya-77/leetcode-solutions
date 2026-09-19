class Solution(object):
    def isPalindrome(self, s):
       a = ""
       for i in s:
            # .isalnum() checks for both letters and numbers
            if i.isalnum():
                a += i
        
        # Reassign the lowercase version back to a
       a = a.lower()
        
        # Check if it reads the same forward and backward
       return a == a[::-1]    
