class Solution(object):
    def tribonacci(self, n):
        ans = [1] * 38
        ans[0] = 0
        ans[1] = 1
        ans[2] = 1

        for i in range(3,n+1):
            ans[i] = ans[i-3] + ans[i-2] + ans[i-1]

        return ans[n]
    
        