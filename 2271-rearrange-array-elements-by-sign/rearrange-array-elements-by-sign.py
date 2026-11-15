class Solution(object):
    def rearrangeArray(self, nums):
        pos = []
        neg = []

        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)

        i = j = 0
        res = []

        while i < len(pos) and j < len(neg):
            res.append(pos[i])
            res.append(neg[j])
            i+=1
            j+=1

        while i < len(pos):
            res.append(pos[i]) 
        while j < len(neg):
            res.append(neg[j])  

        return res        

        