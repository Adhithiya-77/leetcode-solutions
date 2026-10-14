class Solution(object):
    def validPalindrome(self, s):
        def func(s,l,r):
            while l <r :
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        l = 0
        r = len(s)-1

        while l<r:
            if s[l] != s[r]:
                return func(s,l,r-1) or func(s,l+1,r)

            r-=1
            l+=1
        return True                     




        