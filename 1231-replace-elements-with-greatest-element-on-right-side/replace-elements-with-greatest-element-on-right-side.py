class Solution(object):
    def replaceElements(self, arr):
        minimum = -1 

        for i in range(len(arr)-1,-1,-1):
            arr[i], minimum = minimum , max(minimum,arr[i])
        return arr     

        