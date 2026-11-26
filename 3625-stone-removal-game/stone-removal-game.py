class Solution:
    def canAliceWin(self, n: int) -> bool:
        win = 0
        can_take = 10

        while n >= 0:
            n-= can_take
            win+=1
            can_take-=1
        return win %2==0    
        