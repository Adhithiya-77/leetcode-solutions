class Solution(object):
    def shipWithinDays(self, weights, days):
        low = max(weights)
        high = sum(weights)
        ans = 0

        while low<=high:
            cap = (low+high)//2

            if self.cancontain(weights,days,cap):
                ans = cap
                high = cap-1
            else:
                low = cap+1  
        return ans          

    def cancontain(self,weights,days,cap):
        d = 1
        w = 0
        for weight in weights:
            if w+weight > cap:
                d+=1
                w = weight
            else:
                w+=weight
        return d<= days                        