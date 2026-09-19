class Solution(object):
    def isPalindrome(self, s):
        a = ""
        for i in s:
            if i.isalnum():
                a+=i.lower()
        right = len(a)-1        
        for j in range(0,len(a)//2):
            if a[j]!= a[right]:
                return False
            right -= 1
        return True        
