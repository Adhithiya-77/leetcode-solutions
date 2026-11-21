class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left <= right :
            if s[left] != s[right] :
                return self.checkpalindrome(s,left+1,right) or self.checkpalindrome(s,left,right-1)

            left +=1
            right -=1
        return True    

    def checkpalindrome(self,s,left,right):
        while left <=right:
            if s[left] != s[right]:
                return False
            left+=1
            right-=1
        return True                     

    
        