class Solution(object):
    def searchMatrix(self, matrix, target):

        if not matrix or not matrix[0]:
            return False
            
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        bottom = len(matrix) -1
        row = -1
        
        while top <= bottom:
            mid = (top + bottom)//2
            if matrix[mid][0] <= target and matrix[mid][n-1] >= target :
                row = mid
                break 
            elif matrix[mid][0] > target:
                bottom = mid-1
            else:
                top = mid+1

        if row == -1:
            return False

        right = n-1
        left = 0

        while left<= right:
            mid = (left+right)//2
            if matrix[row][mid]== target:
                return True
            elif matrix[row][mid] > target:
                right = mid-1
            else:
                left = mid+1

        return False               

                                


       
        