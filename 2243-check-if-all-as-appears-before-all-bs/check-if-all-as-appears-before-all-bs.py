class Solution:
    def checkString(self, s: str) -> bool:
        b_count = 0

        for i in s:
            if i == "a" and b_count >0:
                return False
            if i == "b":
                b_count+=1
        return True            
        