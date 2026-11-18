class Solution(object):
    def findLucky(self, arr):
        b = sorted(set(arr),reverse= True)
        for i in b:
            if arr.count(i)==i:
                return i
        return -1        
        