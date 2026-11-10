class Solution(object):
    def isPalindrome(self, x):
        ab = str(x)
        bc = ab[::-1]   # Reverse the string
        if ab == bc:
            return True
        else:
            return False
