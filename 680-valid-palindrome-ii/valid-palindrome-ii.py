class Solution(object):
    def validPalindrome(self, s):
        def fuc(s,l,r):
            while l<r:
                if s[l] != s[r]:
                   return False
                l+=1
                r-=1
            return True

        l = 0
        r = len(s)-1
        while l<r:
            if s[l] != s[r]:
                return fuc(s,l,r-1) or fuc (s,l+1,r)
            l+=1
            r-=1
        return True    




        